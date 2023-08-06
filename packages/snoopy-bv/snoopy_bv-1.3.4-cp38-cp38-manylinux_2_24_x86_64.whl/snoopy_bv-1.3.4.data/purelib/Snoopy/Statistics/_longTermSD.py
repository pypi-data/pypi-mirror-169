"""Convenience function to compute long-term value on a scatter-diagram

Work In Progress

"""

from Snoopy import Spectral as sp
from Snoopy import Statistics as st
from matplotlib import pyplot as plt


class LongTermSD( ):

    def __init__(self, rao , sd, nb_hstep, gamma, spreadingType = sp.SpreadingType.No, spreadingValue = 3., dss = 10800, sht_engine = "SpectralMoments"):
        """Compute long-term value, using scatter-diagram and RAO as input.

        Parameters
        ----------
        rao : sp.Rao
            RAO, ready for spectral calculation (symmetrized). Can contain several 'mode'
        sd : DiscreteSD
            The scatter diagram
        nb_hstep : integer
            Number of heading step (36 would lead to a 10 degree step).
        gamma : float
            gamma value for Jonswap spectrum.
        spreadingType : sp.spreadingType
            Spreading type
        spreadingValue : float
            Spreading value
        dss : float, optional
            Sea-state duration. The default is 10800.

        Example
        -------
        >>> lt_sd = LongTermSD(rao, rec34_SD, 36 , 1.5, spreadingType = sp.SpreadingType.Cosn, spreadingValue=3.0)
        >>> extreme_25_years = lt_sd.rp_to_x(25.0)

        """

        self.rao = rao
        self.sd = sd
        self.nb_hstep = nb_hstep
        self.dss = dss
        self.sht_engine = sht_engine

        ssList = self.sd.to_seastate_list(headingList=nb_hstep , gamma = gamma , spreadingType=spreadingType, spreadingValue = spreadingValue)

        self.ss_df = sp.SeaStatesDF.FromSeaStateList( ssList )

        self._m0s_m2s = None
        self._lt = None


    def _get_default_i_rao(self, i_rao) :
        if i_rao is None :
            if (self.rao.getNModes() == 1) :
                return 0
            else :
                raise(ValueError("Index of RAO should be provided" ) )
        else :
            return i_rao


    @property
    def longTerm(self):
        if self._lt is None :
            m0s, m2s = self.m0s_m2s
            shtStats = sp.SpectralStats( m0 = m0s[:,:] , m2 = m2s[:,:] )
            self._lt = [st.LongTermSpectral( shtStats.Rs[:,i] , shtStats.Rtz[:,i], probabilityList = self.ss_df.PROB.values, dss = self.dss ) for i in range(self.rao.getNModes()) ]
        return self._lt

    @property
    def m0s_m2s(self) :
        if self._m0s_m2s is None:
            self._m0s_m2s = self.ss_df.computeSpectral(self.rao, linear_hs=True, progressBar=True, engine = self.sht_engine)
        return self._m0s_m2s



    @m0s_m2s.setter
    def m0s_m2s(self, m0s_m2s):
        #TODO: check ?
        self._m0s_m2s = m0s_m2s


    def x_to_p(self, x, *args, **kwargs):
        """Return non-exceedance probability of x.

        Parameters
        ----------
        x: float
            Respones Value
        duration: float
            Long term duration (in year)

        Returns
        -------
        list
            Non-exceedance probability (on all 'mode' in the RAO)
        """

        return [lt.x_to_p(x, *args, **kwargs) for lt in self.longTerm ]

    def rp_to_x(self,rp):
        """Compute return values corresponding to return period rp

        Parameters
        ----------
        rp : float
            Return period, in year.

        Returns
        -------
        list(float)
            Return values
        """
        return [lt.rp_to_x(rp) for lt in self.longTerm ]


    def p_to_x(self, p, *args, **kwargs):
        """Return the non-exceedance probability of x in duration (year).

        Parameters
        ----------
        x: float
            Respones Value
        duration: float
            Long term duration (in year)

        Returns
        -------
        list(float)
            cdf  (i.e.  P( x < X )  )
        """

        return [lt.p_to_x(p, *args, **kwargs) for lt in self.longTerm ]


    def contribution_df(self, x, i_rao = None):
        """Return contribution as dataframe.

        Parameters
        ----------
        x : float or array
            Extreme value
        i_rao : int or None, optional
            Index of RAO of interest. The default is None.

        Returns
        -------
        pd.DataFrame
            Sea-state dataframe with contribution added as "Contribution_RAO_i" column

        """

        res = self.ss_df.copy()
        if hasattr(x, "__len__") :
            for i, x_ in enumerate(x):
                res.loc[:,f"Contribution_RAO_{i:}"] = self.longTerm[i].contribution(x_)
        else :
            i_rao = self._get_default_i_rao(i_rao)
            res.loc[:,f"Contribution_RAO_{i_rao:}"] = self.longTerm[i_rao].contribution(x)
        return res


    def plot_contribution( self, x, how = "heading" , i_rao = None, ax = None, **kwargs):
        from droppy import pyplotTools as dplt
        if ax is None :
            fig, ax = plt.subplots()

        i_rao = self._get_default_i_rao(i_rao)

        contrib_df = self.contribution_df( x , i_rao = i_rao )

        if how == "heading" :
            contrib_df.groupby("Heading_0").sum().loc[ : , f"Contribution_RAO_{i_rao:}" ].plot(ax=ax, **kwargs)
        elif how == "hs_tp" :
            df = contrib_df.groupby( ["hs_0", "tp_0"] ).sum().loc[ : , f"Contribution_RAO_{i_rao:}" ].unstack()
            dplt.dfSurface(df, ax=ax, **kwargs)

        else:
            raise(ValueError( f"'how must be within ['heading' , 'hs_tp'']. Got : {how:}" ))



if __name__ ==  "__main__" :

    from Pluto.ScatterDiagram import rec34_SD

    rao = sp.Rao( f"{sp.TEST_DATA:}/my_10.rao").getRaoForSpectral()

    raos = sp.Rao( [ sp.Rao( f"{sp.TEST_DATA:}/my_10.rao").getRaoForSpectral(),  sp.Rao( f"{sp.TEST_DATA:}/my_10.rao").getRaoForSpectral() ] )

    lt_sd = LongTermSD(rao, rec34_SD, 36 , 1.5, spreadingType = sp.SpreadingType.Cosn, spreadingValue=3.0)

    lt_sd.rp_to_x(25.0)

    lt_sd.plot_contribution( lt_sd.rp_to_x( 25.0), how = "heading" )
    lt_sd.plot_contribution( lt_sd.rp_to_x( 25.0), how = "hs_tp" )

