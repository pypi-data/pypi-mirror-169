import os
import sys
import pandas as pd
from pathlib import Path
from GMXMMPBSA.API import MMPBSA_API
from GMXMMPBSA.exceptions import NoFileExists


def parse_GMXMMPBSA_RESULTS(mmxsafile, outdir='.'):
    if not isinstance(mmxsafile, Path):
        fname = Path(mmxsafile)

    if not fname.exists():
        raise NoFileExists("cannot find %s!" % fname)
    os.chdir(fname.parent)
    d_mmpbsa = MMPBSA_API()
    d_mmpbsa.setting_time()
    d_mmpbsa.load_file(fname)

    # Final energy
    data = d_mmpbsa.get_energy(remove_empty_terms=False)['data']['normal']
    deltaG = None
    frame_list = d_mmpbsa.frames_list
    for key, df in data.items():
        complex = df['complex'].loc[frame_list, 'TOTAL']
        receptor = df['receptor'].loc[frame_list, 'TOTAL']
        ligand = df['ligand'].loc[frame_list, 'TOTAL']

        internal = df['delta'].loc[frame_list, ["BOND","ANGLE","DIHED"]].sum(axis=1)
        vdw = df['delta'].loc[frame_list, ["VDWAALS","1-4 VDW"]].sum(axis=1)
        eel = df['delta'].loc[frame_list, ["EEL","1-4 EEL"]].sum(axis=1)

        if key == 'pb':
            polar = df['delta'].loc[frame_list, "EPB"]
            nonpolar = df['delta'].loc[frame_list, ["ENPOLAR","EDISPER"]].sum(axis=1)
        elif key == 'gb':
            polar = df['delta'].loc[frame_list, "EGB"]
            nonpolar = df['delta'].loc[frame_list, "ESURF"]
        gas = df['delta'].loc[frame_list, "GGAS"]
        sol = df['delta'].loc[frame_list, "GSOLV"]
        total = df['delta'].loc[frame_list, "TOTAL"]
        dic = {
            'mode':[key]*len(frame_list),
            'complex':complex,
            'receptor':receptor,
            'ligand':ligand,
            'Internal':internal,
            'Van der Waals':vdw,
            'Electrostatic':eel,
            'Polar Solvation':polar,
            'Non-Polar Solvation':nonpolar,
            'Gas':gas,
            'Solvation':sol,
            'TOTAL':total
        }
        if deltaG is None:
            deltaG = pd.DataFrame(dic)
        else:
            deltaG = pd.concat([deltaG, pd.DataFrame(dic)])
    
    # Decomposition energy
    resG = None
    data = d_mmpbsa.get_decomp_energy()['data']
    if len(data) != 0:
        data = data['normal']
        header =  ['resid', 'mode', 'Internal', 'Van der Waals', 'Electrostatic', 'Polar Solvation', 'Non-Polar Solvation', 'TOTAL']
        for key,df in data.items():
            reskeys = set([k[0] for k in df['delta']['TDC'].columns if k[1]=='tot'])
            for reskey in reskeys:
                internal = df['delta']['TDC'][reskey].loc[frame_list, 'int']
                vdw  = df['delta']['TDC'][reskey].loc[frame_list, 'vdw']
                eel = df['delta']['TDC'][reskey].loc[frame_list, 'eel']
                polar = df['delta']['TDC'][reskey].loc[frame_list, 'pol']
                nonpolar  = df['delta']['TDC'][reskey].loc[frame_list, 'sas']
                total  = df['delta']['TDC'][reskey].loc[frame_list, 'tot']
                dic = {
                    'resid':[reskey]*len(frame_list),
                    'mode':[key]*len(frame_list),
                    'Internal':internal,
                    'Van der Waals':vdw,
                    'Electrostatic':eel,
                    'Polar Solvation':polar,
                    'Non-Polar Solvation':nonpolar,
                    'TOTAL':total
                }
                if resG is None:
                    resG = pd.DataFrame(dic)
                else:
                    resG = pd.concat([resG, pd.DataFrame(dic)])
    energyfile = os.path.join(outdir, 'Energy.csv')
    decfile = os.path.join(outdir, 'Dec.csv')
    deltaG.to_csv(energyfile)
    if resG is not None:
        resG.to_csv(decfile)
