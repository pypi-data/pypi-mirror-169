modelmeta = {
    'csm':
    {
        'engine': 'bol_main',
        'alias':
        [
            'csm1',
        ],
        'description': 'CSM fit',
        'func': 'functions.csm_interaction_bolometric', 
        'parname':        
        [
            r'$M_\mathrm{ej}$', r'$M_\mathrm{csm}$',
            r"$v_\mathrm{ej}$", r'$\eta$',
            r"$\rho$", r'$\kappa$', r'$r_\mathrm{0}$',
            r'$t_\mathrm{fl}$',
        ],
        'par' :
        [
            'mej', 'csm_mass', 'vej', 'eta', 'rho', 'kappa', 'r0', 'texp',
        ],
        'bestv':
        {
            'mej' : 5,
            'csm_mass' : 5,
            'vej' : 6,
            'eta' : 1e-1,
            'rho' : 1e-3,
            'kappa' : 0.07,
            'r0' : 100,
            'texp' : -18,
        },
        'bounds':
        {
            'mej' : [.1, 100],
            'csm_mass' : [0, 100],
            'vej' : [2, 40],
            'eta' : [0, 1],
            'rho' : [0, 1],
            'kappa' : [0, 0.3],
            'r0' : [1, 1000],
            'texp' : [-100, 0],
        },
    },    
}
