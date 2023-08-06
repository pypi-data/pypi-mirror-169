import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Snoopy.Math import edges_from_center, get_dx
from Snoopy import Spectral as sp
from Snoopy import logger

"""
   Function related to discrete scatter diagram.

   Storage type is a pandas.DataFrame, with Hs as index and Tp/Tz as columns. The type of wave period is indicated by the index name

"""


class DiscreteSD( pd.DataFrame ) :

    @classmethod
    def FromTimeSeries(cls, hs, T, hsEdges = np.arange(0,21,0.5), tEdges =  np.arange(1,21,0.5) , T_name = None ) :
        """Construct scatter-diagram from time series.

        No extrapolation is done, this is simply a 2D histogram

        Parameters
        ----------
        hs : np.ndarray
            Hs time-serie
        T : np.ndarray
            Period Hs time-serie
        hsEdges : np.ndarray, optional
            Edges for Hs. The default is np.arange(0,21,0.5).
        tEdges : np.ndarray, optional
            Edges for period. The default is np.arange(1,21,0.5).
        T_name : str, optional
            Name of the period, among ["tz" , "t0m1" , "tp"]. The default is None.

        Returns
        -------
        DiscreteSD
            The scatter-diagram

        """
        data_, hsEdges_, tzEdges_ = np.histogram2d( hs, T , bins = [ hsEdges , tEdges ] )
        sdDiscrete = pd.DataFrame( data = data_, index = 0.5*(hsEdges_[:-1] + hsEdges_[1:]), columns = 0.5*(tzEdges_[:-1] + tzEdges_[1:])  )
        sdDiscrete.index.name = "hs"
        sdDiscrete.columns.name = T_name
        return cls(sdDiscrete)

    def __init__(self, *args, **kwargs) :
        """init as standard pandas DataFrame, just ensure that index and columns are float.
        """
        pd.DataFrame.__init__(self, *args, **kwargs)
        if self.columns.dtype == np.dtype("O") :
            self.columns = self.columns.astype(float)
        if self.index.dtype == np.dtype("O") :
            self.index = self.index.astype(float)

    @property
    def _constructor(self):
        return DiscreteSD

    @property
    def dv1( self ):
        return self.index[1] - self.index[0]

    @property
    def n( self ):
        return self.sum().sum()

    @property
    def nv2( self ):
        return len(self.columns)

    @property
    def nv1( self ):
        return len(self.index)

    @property
    def v2name(self):
        return self.columns.name


    @property
    def dv2( self ):
        return self.columns[1] - self.columns[0]

    def makeProbabilityDensity(self):
        """Scale probability so that values are probability density. (integral == 1)
        """
        self /= self.sum().sum() * self.dv1 * self.dv2


    def plotSD(self, ax = None, linewidths= 1.0, density = False, **kwargs) :
        """Plot the scatter diagram

        Parameters
        ----------
        ax : plt.Axes, optional
            Where to plot. The default is None.
        linewidths : float, optional
            Spacing between cells. The default is 1.0.
        **kwargs : any
            Argument passed to seaborn.heatmap

        Returns
        -------
        ax : plt.Axes
            The plot

        Example
        -------
        To get plot with number in each cell :

        >>> sd.plotSD( annot=True, ax=ax, fmt = ".2f", annot_kws = {"fontdict":{"size":8}}, cbar=False), norm=colors.LogNorm(vmin=1e-10, vmax=sd.max().max()), clip = True) )
        """

        import seaborn as sns

        if ax is None :
            fig, ax = plt.subplots()

        sd = self.sort_index(ascending = False, axis = 0)

        sns.heatmap( sd,
                     linewidths = linewidths,
                     ax=ax,
                     **kwargs
                     )
        return ax



    def iso_probability(self , p):
        return self.iso_value(  p * self.sum().sum()  * self.dv1*self.dv2 )


    def iso_value(self , v):
        """Return ISO probability contour

        Parameters
        ----------
        v : float
            Value

        Returns
        -------
        hs : np.ndarray
            Hs
        tx : np.ndarray
            Period
        """

        from skimage import measure
        from scipy.interpolate import InterpolatedUnivariateSpline
        cont = measure.find_contours(self.values, v)[0]
        hs = InterpolatedUnivariateSpline(  np.arange( 0 , len(self), 1)  , self.index.values )( cont[:,0]  )
        tx = InterpolatedUnivariateSpline(  np.arange( 0 , len(self.columns), 1)  , self.columns.values )( cont[:,1]  )
        return hs , tx



    def iform_iso(self , p) :
        """Return contour based on RP-C205

        Note that this has very little interest over standard iform, which should be prefered.

        1- Find Hs with exceedance probability p
        2- Find probability density for this Hs
        3- Get iso density contour

        Parameters
        ----------
        p : float
            Probability

        Returns
        -------
        Tuple of array
            The contour
        """
        from Pluto.statistics.ecdf import Empirical
        empHs = Empirical.FromBinCounts( *self.get_v1_edges_count() )
        hs = empHs.isf( p )
        logger.debug(f"IFORM_ISO, Hs = {hs:}")
        hs_r = self.index[ self.index.get_loc( float(hs) , method = "nearest" ) ]

        # Get V2 at hs location
        t = self.get_v2_conditional_pdf( hs_r ).idxmax()
        p_density = self.loc[ hs_r, t ]
        return self.iso_value( p_density )


    def toStarSpec(self, gamma = None):
        """Convert to starspec

        Parameters
        ----------
        gamma : float, optional
            gamma value. Used to convert period to something handled by StarSpec. The default is None.

        Returns
        -------
        str
            The scatter-diagram, in StarSpec format

        """
        t_def = self.columns.name.lower()
        return toStarSpec(self , period = t_def, gamma = gamma )


    def get_v1_pdf(self) :
        hs_hist = self.sum(axis = 1)
        return hs_hist / (hs_hist.sum()*self.dv1)

    def get_v1_cdf(self):
        edges = self.get_v1_edges()
        return pd.Series( np.insert( np.cumsum( self.sum(axis = 1 )) , 0 , 0. ) / self.n , index = edges )

    def get_v1_sf(self):
        hs_pdf = self.get_v1_pdf()
        return pd.Series(  1. - np.cumsum( hs_pdf.values )*self.dv1, index = self.index.values + self.dv1*0.5 )


    def sample(self , n = 1) :
        a = (self.stack()*n).astype(int)
        n_tot = a.sum() * n
        s = np.zeros( (n_tot, 2), dtype = float )
        i = 0
        for ht, n in a.iteritems() :
            s[i:i+n, 0] = ht[0]
            s[i:i+n, 1] = ht[1]
            i += n
        return s

    def get_v1_edges(self):
        return edges_from_center(self.index.values)

    def get_v2_edges(self):
        return edges_from_center(self.columns.values)

    def get_v1_edges_count(self):
        return edges_from_center(self.index.values) , self.sum(axis = 1.).values


    def getCountScatterDiagram(self, n = None ):
        if n is None :
            n = self.sum().sum()  # Just make the scatter diagram as integer
        sd_count = self * n / self.n
        sd_count = sd_count.round(0).astype(int)
        return sd_count


    def getAggregated(self , new_edges , axis = 0, eps = 0.001 ):
        """Aggregate scatter-diagram by larger bins.

        Parameters
        ----------
        new_edges : np.ndarray
            New bin edges.
        axis : int, optional
            Axis. The default is 0.
        eps : float, optional
            Tolerance. The default is 0.001.

        Returns
        -------
        DiscreteSd
            Aggregated scatter-diagram.
        """


        if isinstance( new_edges , int) :
            old_edges = edges_from_center(self.axes[axis])
            new_edges = old_edges[::new_edges]
            if new_edges[-1] < old_edges[-1] :
                new_edges = np.append( new_edges, 2*new_edges[-1]-new_edges[-2] )

        newCenter = (new_edges[:-1] + new_edges[1:])*0.5
        dtype = self.dtypes.values[0]
        if axis == 0 :
            newSd = self.__class__( index = pd.Index(newCenter , name = self.index.name) , columns = self.columns  )
            for i, c in enumerate(newCenter) :
                newSd.loc[c , : ] = self.loc[ new_edges[i]+eps : new_edges[i+1]-eps , :  ].sum()
                newSd.loc[c , : ] += self.loc[ new_edges[i+1]-eps : new_edges[i+1]+eps , :  ].sum() * 0.5
                newSd.loc[c , : ] += self.loc[ new_edges[i]-eps : new_edges[i]+eps , :  ].sum() * 0.5
        elif axis == 1 :
            newSd = self.__class__( index = self.index, columns = pd.Index(newCenter , name = self.columns.name ))
            for i, c in enumerate(newCenter) :
                newSd.loc[: , c ] = self.loc[ : , new_edges[i] + eps : new_edges[i+1] - eps  ].sum(axis = 1)
                newSd.loc[: , c ] += self.loc[ : , new_edges[i]-eps:new_edges[i] + eps  ].sum(axis = 1) * 0.5
                newSd.loc[: , c ] += self.loc[ : , new_edges[i+1]-eps:new_edges[i+1] + eps  ].sum(axis = 1) * 0.5

        #Check that total count is there
        if not ( np.isclose(  self.n , newSd.n) ) :
            print (self.n , newSd.n)
            raise(Exception("Problem in aggregating the scatter diagram"))

        return self.__class__(newSd).astype(dtype)

    def makeEven( self, dv1 = None , dv2 = None ):
        """Make the bin size constant.
        """
        #TODO : use "getAggregated" ?

        if dv1 is None :
            dv1 = np.min(np.diff( self.index.values ))

        newIndex = np.arange( self.index.values[0] , self.index.values[-1] , dv1 )
        for i in newIndex :
            if i not in self.index :
                if np.min(np.abs(self.index - i)) > 1e-5 :
                    self.loc[i , :] = np.zeros( (self.nv2), dtype = float )

        self.sort_index(inplace = True)

        if dv2 is None :
            dv2 = np.min(np.diff( self.columns.values ))
        newIndex = np.arange( self.columns.values[0] , self.columns.values[-1] , dv2 )
        for i in newIndex :
            if i not in self.columns :
                if np.min(np.abs(self.columns - i)) > 1e-5 :
                    self.loc[: , i] = np.zeros( (self.nv1), dtype = float )
        self.sort_index(axis = 1, inplace = True)


    def isEvenlySpaced(self, tol) :
        if get_dx(self.index.values, tol ) is None:
            return False
        if get_dx(self.columns.values, tol ) is None:
            return False
        return True

    def get_v2_conditional_pdf(self , v1, method = None):
        ihs = self.index.get_loc( v1, method = method )
        return (self.iloc[ihs,:] / (self.iloc[ihs,:].sum() * self.dv2) )


    def get_v2_conditional_sf(self, v1):
        t_pdf = self.get_v2_conditional_pdf(v1)
        return pd.Series(  1. - np.cumsum( t_pdf.values )*self.dv2, index = self.columns.values + self.dv2 * 0.5 )

    def getWithoutZeros(self):
        sdNew = self.loc[ self.sum(axis = 1) > 0 , :].copy(deep=True)
        sdNew = sdNew.loc[ :, sdNew.sum(axis = 0) > 0 ]
        return sdNew


    def to_seastate_list(self, headingList, gamma , spreadingType , spreadingValue ):
        """Create list of Jonswap sea-state from scatter-diagram

        Parameters
        ----------
        headingList : array like or int
            List of headings
        gamma : float
            Gamma value.
        spreadingType : sp.SpreadingType
            Spreading function
        spreadingValue : float
            Spreading value

        Raises
        ------
        ValueError
            If period is not 'tp', 'tz' or 't0m1'.

        Returns
        -------
        ssList : list( sp.SeaState )
            List of sea-state
        """

        if isinstance(headingList , int) :
            headingList = np.linspace( 0 , np.pi*2 , headingList, endpoint = False )
            probList = np.full( (len(headingList)) , 1. / len(headingList) )
        elif len( np.array( headingList ).shape ) == 1 :
            probList = np.full( (len(headingList)) , 1. / len(headingList) )
        elif len( np.array( headingList ).shape ) == 2 :
            probList = headingList[:,1]
            headingList = headingList[:,0]
        else :
            raise(Exception())

        ssList = []
        for hs, row in self.iterrows():
            for t, prob in row.items():
                if self.columns.name.lower() == 'tp':
                    tp = t
                elif self.columns.name.lower() == 'tz':
                    tp = sp.Jonswap.tz2tp(t,gamma)
                elif self.columns.name.lower() == 't0m1':
                    tp = sp.Jonswap.t0m12tp(t,gamma)
                else:
                    raise ValueError("Scatter diagram columns name should be either 'Tp', 'Tz' or 'T0m1', not {self.columns.name:}")

                for head, prob_head in zip(headingList, probList):
                    spec = sp.Jonswap(hs=hs, tp=tp, gamma = gamma,  heading = head, spreading_type = spreadingType , spreading_value = spreadingValue )
                    ss = sp.SeaState( spec , probability = prob * prob_head )
                    ssList.append(ss)
        return ssList

    def getTruncated(self , hsMax ):
        """Remove data above hsMax, and report the probablility to Hs = 0. (the ship stay in the port !)

        Parameters
        ----------
        hsMax : float
            Maximum allowed Hs

        Returns
        -------
        DiscreteSD, float
            Truncated scatter diagram, fraction of time below hsMax
        """
        return truncate(self, hsMax)


"""
Functional API kept for compatibility purpose
"""

def toStarSpec(data, period=None, gamma = None):

    # Return a string compatible with StarSpec format
    nHs, nTz = data.shape

    if period is None :
        period = data.columns.name
        logger.info(f"Period for scatter diagram set to {period:}")

    if period.lower() == "tz":
        tList = data.columns.values
        str_ = "SCATTER NB_HS  {}  NB_TZ   {}\n".format(nHs, nTz)
    elif period.lower() == "tp":
        tList = data.columns.values
        str_ = "SCATTER NB_HS  {}  NB_TP   {}\n".format(nHs, nTz)
    elif period.lower() == "t0m1":
        tList = sp.Jonswap.t0m12tp( data.columns.values , gamma = gamma )
        if gamma is None :
            raise(Exception("toStarSpec : gamma required to convert from T0m1" ))
        str_ = "SCATTER NB_HS  {}  NB_TP   {}\n".format(nHs, nTz)
    else :
        raise(Exception(f"Do not know how to convert {period:} to Tp"))

    for t in tList :
        str_ += "{:.3f}  ".format(t)

    str_ += "\n"
    pFormat = "{:.3e} " * (nTz - 1) + "{:.3e}\n"
    for i in data.index:
        str_ += "{:.3f} ".format(i) + pFormat.format(*data.loc[i, :])
    str_ += "ENDSCATTER\n"
    return str_


def getMarginalHs( table ):
    nHs = table.shape[0]
    sf, densityHs = np.zeros((nHs), dtype = "float64"), np.zeros((nHs), dtype = "float64")
    for iHs in range( nHs  ) :
        densityHs[iHs] = table.iloc[iHs , :].sum()
        sf[iHs] = 1. - np.sum( densityHs[0:iHs] )

    d_hs = table.index.values[1] - table.index.values[0]

    return table.index.values - d_hs/2. , sf


def truncate(table, hsMax):
    """Remove data above hsMax, and report the probablility to Hs = 0. (the ship stay in the port !)
    """
    below = table.loc[:hsMax, :].copy()
    ratio = below.sum().sum() / table.sum().sum()
    below.loc[0.] = below.sum(axis=0) * (1 - ratio) / ratio
    below.sort_index(inplace=True)
    return below, ratio



def removeZeros( sd ):
    sdNew = sd.loc[ sd.sum(axis = 1) > 0 , :]
    sdNew = sdNew.loc[ :, sdNew.sum(axis = 0) > 0 ]
    return sdNew



# TODO : Move in data/*.csv

tz_ = [1.5 ,  2.5 ,  3.5 ,  4.5 ,  5.5 ,  6.5 ,  7.5 ,  8.5  , 9.5 ,  10.5 ,  11.5 ,  12.5  , 13.5 ,  14.5 ,  15.5 ,  16.5 ,  17.5 ,  18.5 ]
hs_ = [0.5  ,1.5  ,2.5  ,3.5  ,4.5  ,5.5  ,6.5  ,7.5  ,8.5  ,9.5,  10.5,  11.5,  12.5,  13.5,  14.5,  15.5  ,16.5  ]
rec34_SD = pd.DataFrame(  index = hs_ , columns = tz_ ,dtype = "float" )
rec34_SD.iloc[0,:]  = [ 0.0  ,   0.0  ,   1.3   ,  133.7  ,   865.6 ,   1186.    ,  634.2   ,  186.3  ,    36.9   ,    5.6  ,     0.7  ,   0.1 ,    0.0   ,    0.0   ,    0.0  ,   0.0  ,     0.0  ,   0.0  ]
rec34_SD.iloc[1,:]  = [ 0.0  ,   0.0  ,   0.0   ,   29.3  ,   986.  ,   4976.    , 7738.    , 5569.7  ,  2375.7   ,  703.5  ,   160.7  ,  30.5 ,    5.1   ,    0.8   ,    0.1  ,   0.0  ,     0.0  ,   0.0  ]
rec34_SD.iloc[2,:]  = [ 0.0  ,   0.0  ,   0.0   ,    2.2  ,   197.5 ,   2158.8   , 6230.    , 7449.5  ,  4860.4   , 2066.   ,   644.5  , 160.2 ,   33.7   ,    6.3   ,    1.1  ,   0.2  ,     0.0  ,   0.0  ]
rec34_SD.iloc[3,:]  = [ 0.0  ,   0.0  ,   0.0   ,    0.2  ,    34.9 ,    695.5   , 3226.5   , 5675.   ,  5099.1   , 2838.   ,  1114.1  , 337.7 ,   84.3   ,   18.2   ,    3.5  ,   0.6  ,     0.1  ,   0.0  ]
rec34_SD.iloc[4,:]  = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     6.  ,    196.1   , 1354.3   , 3288.5  ,  3857.5   , 2685.5  ,  1275.2  , 455.1 ,  130.9   ,   31.9   ,    6.9  ,   1.3  ,     0.2  ,   0.0  ]
rec34_SD.iloc[5,:]  = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     1.  ,     51.    ,  498.4   , 1602.9  ,  2372.7   , 2008.3  ,  1126.   , 463.6 ,  150.9   ,   41.    ,    9.7  ,   2.1  ,     0.4  ,   0.1  ]
rec34_SD.iloc[6,:]  = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.2 ,     12.6   ,  167.    ,  690.3  ,  1257.9   , 1268.6  ,   825.9  , 386.8 ,  140.8   ,   42.2   ,   10.9  ,   2.5  ,     0.5  ,   0.1  ]
rec34_SD.iloc[7,:]  = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      3.    ,   52.1   ,  270.1  ,   594.4   ,  703.2  ,   524.9  , 276.7 ,  111.7   ,   36.7   ,   10.2  ,   2.5  ,     0.6  ,   0.1  ]
rec34_SD.iloc[8,:]  = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.7   ,   15.4   ,   97.9  ,   255.9   ,  350.6  ,   296.9  , 174.6 ,   77.6   ,   27.7   ,    8.4  ,   2.2  ,     0.5  ,   0.1  ]
rec34_SD.iloc[9,:]  = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.2   ,    4.3   ,   33.2  ,   101.9   ,  159.9  ,   152.2  ,  99.2 ,   48.3   ,   18.7   ,    6.1  ,   1.7  ,     0.4  ,   0.1  ]
rec34_SD.iloc[10,:] = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.0   ,    1.2   ,   10.7  ,    37.9   ,   67.5  ,    71.7  ,  51.5 ,   27.3   ,   11.4   ,    4.   ,   1.2  ,     0.3  ,   0.1  ]
rec34_SD.iloc[11,:] = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.0   ,    0.3   ,    3.3  ,    13.3   ,   26.6  ,    31.4  ,  24.7 ,   14.2   ,    6.4   ,    2.4  ,   0.7  ,     0.2  ,   0.1  ]
rec34_SD.iloc[12,:] = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.0   ,    0.1   ,    1.   ,     4.4   ,    9.9  ,    12.8  ,  11.  ,    6.8   ,    3.3   ,    1.3  ,   0.4  ,     0.1  ,   0.0  ]
rec34_SD.iloc[13,:] = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.0   ,    0.0   ,    0.3  ,     1.4   ,    3.5  ,     5.   ,   4.6 ,    3.1   ,    1.6   ,    0.7  ,   0.2  ,     0.1  ,   0.0  ]
rec34_SD.iloc[14,:] = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.0   ,    0.0   ,    0.1  ,     0.4   ,    1.2  ,     1.8  ,   1.8 ,    1.3   ,    0.7   ,    0.3  ,   0.1  ,     0.0  ,   0.0  ]
rec34_SD.iloc[15,:] = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.0   ,    0.0   ,    0.0  ,     0.1   ,    0.4  ,     0.6  ,   0.7 ,    0.5   ,    0.1   ,    0.1  ,   0.1  ,     0.0  ,   0.0  ]
rec34_SD.iloc[16,:] = [ 0.0  ,   0.0  ,   0.0   ,    0.0  ,     0.0 ,      0.0   ,    0.0   ,    0.0  ,     0.0   ,    0.1  ,     0.2  ,   0.2 ,    0.2   ,    0.1   ,    0.1  ,   0.0  ,     0.0  ,   0.0  ]
rec34_SD.name = "Rec. 34"
rec34_SD = rec34_SD.rename_axis( "Hs" ).rename_axis("Tz", axis = 1)
rec34_SD = DiscreteSD(rec34_SD)


tz_ = [3.5  ,   4.5  ,   5.5  ,   6.5  ,   7.5 ,    8.5  ,   9.5 ,    10.5 ,   11.5  ,  12.5 ,   13.5   , 14.5,    15.5  ,  16.5  ,  17.5]
hs_ = [ 1 , 2,  3,  4,  5,  6,  7,  8,  9,  10,  11,  12,  13,  14]
ww_SD = pd.DataFrame(  index = hs_ , columns = tz_  ,dtype = "float" )
ww_SD.iloc[0,:]  = [    311   ,  2734  ,  6402 ,   7132  ,  5071 ,   2711 ,   1202  ,  470  ,   169    , 57   ,   19  ,    6     ,  2   ,    1  ,     0   ]
ww_SD.iloc[1,:]  = [    20    ,  764   ,  4453 ,   8841  ,  9045 ,   6020 ,   3000  ,  1225 ,   435    , 140  ,   42  ,    12    ,  3   ,    1  ,     0   ]
ww_SD.iloc[2,:]  = [    0     ,  57    ,  902  ,   3474  ,  5549 ,   4973 ,   3004  ,  1377 ,   518    , 169  ,   50  ,    14    ,  4   ,    1  ,     0   ]
ww_SD.iloc[3,:]  = [    0     ,  4     ,  150  ,   1007  ,  2401 ,   2881 ,   2156  ,  1154 ,   485    , 171  ,   53  ,    15    ,  4   ,    1  ,     0   ]
ww_SD.iloc[4,:]  = [    0     ,  0     ,  25   ,   258   ,  859  ,   1338 ,   1230  ,  776  ,   372    , 146  ,   49  ,    15    ,  4   ,    1  ,     0   ]
ww_SD.iloc[5,:]  = [    0     ,  0     ,  4    ,   63    ,  277  ,   540  ,   597   ,  440  ,   240    , 105  ,   39  ,    13    ,  4   ,    1  ,     0   ]
ww_SD.iloc[6,:]  = [    0     ,  0     ,  1    ,   15    ,  84   ,   198  ,   258   ,  219  ,   136    , 66   ,   27  ,    10    ,  3   ,    1  ,     0   ]
ww_SD.iloc[7,:]  = [    0     ,  0     ,  0    ,   4     ,  25   ,   69   ,   103   ,  99   ,   69     , 37   ,   17  ,    6     ,  2   ,    1  ,     0   ]
ww_SD.iloc[8,:]  = [    0     ,  0     ,  0    ,   1     ,  7    ,   23   ,   39    ,  42   ,   32     , 19   ,   9   ,    4     ,  1   ,    1  ,     0   ]
ww_SD.iloc[9,:]  = [    0     ,  0     ,  0    ,   0     ,  2    ,   7    ,   14    ,  16   ,   14     , 9    ,   5   ,    2     ,  1   ,    0  ,     0   ]
ww_SD.iloc[10,:] = [    0     ,  0     ,  0    ,   0     ,  1    ,   2    ,   5     ,  6    ,   6      , 4    ,   2   ,    1     ,  1   ,    0  ,     0   ]
ww_SD.iloc[11,:] = [    0     ,  0     ,  0    ,   0     ,  0    ,   1    ,   2     ,  2    ,   2      , 2    ,   1   ,    1     ,  0   ,    0  ,     0   ]
ww_SD.iloc[12,:] = [    0     ,  0     ,  0    ,   0     ,  0    ,   0    ,   1     ,  1    ,   1      , 1    ,   0   ,    0     ,  0   ,    0  ,     0   ]
ww_SD.iloc[13,:] = [    0     ,  0     ,  0    ,   0     ,  0    ,   0    ,   0     ,  0    ,   1      , 0    ,   0   ,    0     ,  0   ,    0  ,     0   ]
ww_SD /= np.sum(ww_SD.values)
ww_SD.name = "World-wide"
ww_SD = ww_SD.rename_axis( "Hs" ).rename_axis("Tz", axis = 1)
ww_SD = DiscreteSD(ww_SD)


if __name__ == "__main__":

    import numpy as np
    import pandas as pd
    logger.setLevel(10)

    rec34_SD.plotSD(cmap = "cividis")


