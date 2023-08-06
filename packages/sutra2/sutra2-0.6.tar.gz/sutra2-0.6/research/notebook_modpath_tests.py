# <markdowncell>
# # Figures for Modpath tutorial


# <codecell>
# set working directory to main directory of package
import codecs
import imp

from matplotlib.pyplot import ylabel
from set_cwd_to_project_root import project_root
from pathlib import Path

from pandas import RangeIndex, read_csv
import pandas as pd
from pandas._testing import assert_frame_equal
import numpy as np
import datetime as dt
import os
import ast  # abstract syntax trees
import sys
import copy
# path = os.getcwd()  # path of working directory
from pathlib import Path

from zmq import zmq_version_info

# Plotting modules
import matplotlib.pyplot as plt
import matplotlib 
import matplotlib.colors as colors

# sutra2 modules    
import sutra2.Analytical_Well as AW
import sutra2.ModPath_Well as mpw
import sutra2.Transport_Removal as TR

# get directory of this file
path = Path(__file__).parent
%load_ext autoreload
%autoreload 2

# # Create research files dir
# researchfiles_dir = os.path.join(path,"test_files")
# if not os.path.exists(researchfiles_dir):
#     os.makedirs(researchfiles_dir)

# modflow executable location
mf_exe = os.path.join(path, "mf2005.exe")
# modpath executable location
mp_exe = os.path.join(path, "mpath7.exe")

# <markdowncell>

# <codecell>
# def test_modpath_run_phreatic_nogravelpack(organism_name = "MS2"):

''' def test_modpath_run_phreatic_nogravelpack(organism_name = "MS2"):
    Phreatic scheme without gravelpack: modpath run.'''

# organism name
organism_name = "MS2"
#@Steven: mag weg uit testing: of final concentration toevoegen (geen echte 'assert'). Deze test (of variant ervan) naar readthedocs --> toon de dataframes
test_phrea = AW.HydroChemicalSchematisation(schematisation_type='phreatic',
                                    computation_method = 'modpath',
                                    what_to_export='all',
                                    removal_function = 'mbo',
                                    well_discharge=-319.4*24,
                                    # vertical_resistance_shallow_aquifer=500,
                                    porosity_vadose_zone=0.38,
                                    porosity_shallow_aquifer=0.35,
                                    porosity_target_aquifer=0.35,
                                    recharge_rate=0.3/365.25,
                                    moisture_content_vadose_zone=0.15,
                                    ground_surface = 22.0,
                                    thickness_vadose_zone_at_boundary=5.0,
                                    thickness_shallow_aquifer=10.0,
                                    thickness_target_aquifer=40.0,
                                    hor_permeability_target_aquifer=35.0,
                                    hor_permeability_shallow_aquifer = 0.02,
                                    thickness_full_capillary_fringe=0.4,
                                    redox_vadose_zone='anoxic', #'suboxic',
                                    redox_shallow_aquifer='anoxic',
                                    redox_target_aquifer='deeply_anoxic',
                                    pH_vadose_zone=5.,
                                    pH_shallow_aquifer=6.,
                                    pH_target_aquifer=7.,
                                    dissolved_organic_carbon_vadose_zone=10., 
                                    dissolved_organic_carbon_shallow_aquifer=4., 
                                    dissolved_organic_carbon_target_aquifer=2.,
                                    fraction_organic_carbon_vadose_zone=0.001,
                                    fraction_organic_carbon_shallow_aquifer=0.0005,
                                    fraction_organic_carbon_target_aquifer=0.0005, 
                                    temp_water=11.,
                                    solid_density_vadose_zone= 2.650, 
                                    solid_density_shallow_aquifer= 2.650, 
                                    solid_density_target_aquifer= 2.650, 
                                    diameter_borehole = 0.75,
                                    name = organism_name,
                                    # diameter_filterscreen = 0.2,
                                    point_input_concentration = 100.,
                                    discharge_point_contamination = 100.,#made up value
                                    top_clayseal = 17,
                                    compute_contamination_for_date=dt.datetime.strptime('2020-01-01',"%Y-%m-%d"),
                                    ncols_near_well = 20,
                                    ncols_far_well = 80,
                                )

test_phrea.make_dictionary()
# Remove/empty point_parameters
test_phrea.point_parameters = {}

# print(test_phrea.__dict__)
modpath_phrea = mpw.ModPathWell(test_phrea,
                        workspace = os.path.join(path,"test2_phrea_nogp"),
                        modelname = "phreatic",
                        bound_left = "xmin",
                        bound_right = "xmax")
# print(modpath_phrea.__dict__)
# Run phreatic schematisation
modpath_phrea.run_model(run_mfmodel = True,
                    run_mpmodel = True)

# Calculate advective microbial removal
modpath_removal = TR.Transport(modpath_phrea,
                                        organism = organism_name)

# Calculate advective microbial removal
# Final concentration per endpoint_id
C_final = {}
for endpoint_id in modpath_phrea.schematisation_dict.get("endpoint_id"):
    df_particle, df_flowline, C_final[endpoint_id] = modpath_removal.calc_advective_microbial_removal(
                                        modpath_phrea.df_particle, modpath_phrea.df_flowline, 
                                        endpoint_id = endpoint_id,
                                        trackingdirection = modpath_phrea.trackingdirection,
                                        mu1 = 0.1151, grainsize = 0.00025, alpha0 = 0.037e-2, pH0 = 7.5,
                                        temp_water = 11., rho_water = 999.703, organism_diam = 2.731e-6,
                                        conc_start = 1., conc_gw = 0.)

# df_particle file name 
particle_fname = os.path.join(modpath_phrea.dstroot,modpath_phrea.schematisation_type + "_df_particle_microbial_removal.csv")
# Save df_particle 
df_particle.to_csv(particle_fname)

# df_flowline file name
flowline_fname = os.path.join(modpath_phrea.dstroot,modpath_phrea.schematisation_type + "_df_flowline_microbial_removal.csv")
# Save df_flowline
df_flowline.to_csv(flowline_fname)



# <codecell>
''' def test_modpath_run_horizontal_flow_diffuse(organism_name = "MS2"):

    Horizontal flow test in target_aquifer: modpath run.'''

# @Steven: deze test in read the docs zodat je zelf kunt visualisren of code klopt
# organism name
organism_name = "MS2"

# well discharge
well_discharge = -1000.
# distance to boundary
distance_boundary = 50.
# Center depth of target aquifer
z_point = 0 - 0.1 - 10.
x_point = distance_boundary - 0.5
# Phreatic scheme without gravelpack: modpath run.
test_conf_hor = AW.HydroChemicalSchematisation(schematisation_type='semiconfined',
                            computation_method = 'modpath',
                            what_to_export='all',
                            removal_function = 'mbo',
                            # biodegradation_sorbed_phase = False,
                            well_discharge= well_discharge,
                            # vertical_resistance_shallow_aquifer=500,
                            porosity_vadose_zone=0.33,
                            porosity_shallow_aquifer=0.33,
                            porosity_target_aquifer=0.33,
                            recharge_rate=0.,
                            moisture_content_vadose_zone=0.15,
                            ground_surface = 0.0,
                            thickness_vadose_zone_at_boundary=0.,
                            thickness_shallow_aquifer=0.1,
                            thickness_target_aquifer=20.0,
                            hor_permeability_target_aquifer=10.0,
                            hor_permeability_shallow_aquifer = 1.,
                            vertical_anisotropy_shallow_aquifer = 1000.,
                            thickness_full_capillary_fringe=0.4,
                            redox_vadose_zone='anoxic', #'suboxic',
                            redox_shallow_aquifer='anoxic',
                            redox_target_aquifer='anoxic',
                            pH_vadose_zone=7.5,
                            pH_shallow_aquifer=7.5,
                            pH_target_aquifer=7.5,
                            dissolved_organic_carbon_vadose_zone=1., 
                            dissolved_organic_carbon_shallow_aquifer=1., 
                            dissolved_organic_carbon_target_aquifer=1.,
                            fraction_organic_carbon_vadose_zone=0.001,
                            fraction_organic_carbon_shallow_aquifer=0.001,
                            fraction_organic_carbon_target_aquifer=0.001, 
                            temp_water=12.,
                            solid_density_vadose_zone= 2.650, 
                            solid_density_shallow_aquifer= 2.650, 
                            solid_density_target_aquifer= 2.650, 
                            diameter_borehole = 0.2,
                            name = organism_name,
                            diameter_filterscreen = 0.2,
                            top_clayseal = 0,
                            compute_contamination_for_date=dt.datetime.strptime('2020-01-01',"%Y-%m-%d"),
                            model_radius = distance_boundary,
                            ncols_near_well = 10,
                            ncols_far_well = int(distance_boundary/5),
                            # Point contamination
                            point_input_concentration = 1.,
                            discharge_point_contamination = abs(well_discharge),
                            distance_point_contamination_from_well = x_point,
                            depth_point_contamination = z_point,
                            )

test_conf_hor.make_dictionary()


# Remove "vadose" layer from geo_parameters
test_conf_hor.geo_parameters.pop("vadose_zone")

### Adjust ibound_parameters to add horizontal flow ###

# Confined top boundary ; no recharge_parameters
test_conf_hor.ibound_parameters.pop("top_boundary1")
test_conf_hor.ibound_parameters.pop("inner_boundary_shallow_aquifer")

# Width (delr) outer boundary cells
delr_outer = 1.

# Add outer boundary for horizontal flow test
test_conf_hor.ibound_parameters["outer_boundary_target_aquifer"] = {
                        'top': test_conf_hor.bottom_shallow_aquifer,
                        'bot': test_conf_hor.bottom_target_aquifer,
                        'xmin': test_conf_hor.model_radius - delr_outer,
                        'xmax': test_conf_hor.model_radius,
                        'ibound': -1
                        }
# concentration_boundary_parameters
test_conf_hor.concentration_boundary_parameters = {'source1': {
            'organism_name': organism_name,
            'xmin': test_conf_hor.model_radius - delr_outer * 0.5,
            'xmax': test_conf_hor.model_radius,
            'zmax': test_conf_hor.bottom_shallow_aquifer,
            'zmin': test_conf_hor.bottom_target_aquifer,
            'input_concentration': test_conf_hor.diffuse_input_concentration
            }
        # 'source2' :{}> surface water (BAR & RBF) #@MartinvdS come back to this when we start this module
        }
# Remove/empty point_parameters
test_conf_hor.point_parameters = {}

# Add point parameters                       
startpoint_id = ["outer_boundary_target_aquifer"]


# ModPath well
modpath_hor = mpw.ModPathWell(test_conf_hor, #test_phrea,
                        workspace = "test4_conf_hor_diffuse",
                        modelname = "confined_hor",
                        bound_left = "xmin",
                        bound_right = "xmax")
# print(modpath_phrea.__dict__)
# Run phreatic schematisation
modpath_hor.run_model(run_mfmodel = True,
                    run_mpmodel = True)

# microbial removal properties
# organism_name = 'MS2'
alpha0 = {"suboxic": 1.e-3, "anoxic": 1.e-5, "deeply_anoxic": 1.e-5}
pH0 = {"suboxic": 6.6, "anoxic": 6.8, "deeply_anoxic": 6.8}
organism_diam =  2.33e-8
mu1 = {"suboxic": 0.149,"anoxic": 0.023,"deeply_anoxic": 0.023}

removal_parameters = {organism_name: 
                {"organism_name": organism_name,
                    "alpha0": alpha0,
                    "pH0": pH0,
                    "organism_diam": organism_diam,
                    "mu1": mu1
                }
            }
# Removal parameters organism
rem_parms = removal_parameters[organism_name]

# Calculate advective microbial removal
modpath_removal = TR.Transport(modpath_hor,
                        organism = organism_name,
                        alpha0_suboxic = rem_parms["alpha0"]["suboxic"],
                        alpha0_anoxic = rem_parms["alpha0"]["anoxic"],
                        alpha0_deeply_anoxic =rem_parms["alpha0"]["deeply_anoxic"],
                        pH0_suboxic =rem_parms["pH0"]["suboxic"],
                        pH0_anoxic =rem_parms["pH0"]["anoxic"],
                        pH0_deeply_anoxic =rem_parms["pH0"]["deeply_anoxic"],
                        mu1_suboxic = rem_parms["mu1"]["suboxic"],
                        mu1_anoxic = rem_parms["mu1"]["anoxic"],
                        mu1_deeply_anoxic = rem_parms["mu1"]["deeply_anoxic"],
                        organism_diam = rem_parms["organism_diam"]
                        )

# Calculate advective microbial removal
# Final concentration per endpoint_id
C_final = {}
for endpoint_id in modpath_hor.schematisation_dict.get("endpoint_id"):
    df_particle, df_flowline, C_final[endpoint_id] = modpath_removal.calc_advective_microbial_removal(
                                        modpath_hor.df_particle, modpath_hor.df_flowline, 
                                        endpoint_id = endpoint_id,
                                        trackingdirection = modpath_hor.trackingdirection,
                                        conc_start = 1., conc_gw = 0.)

# df_particle file name 
particle_fname = os.path.join(modpath_hor.dstroot,modpath_hor.schematisation_type + "_df_particle_microbial_removal.csv")
# Save df_particle 
df_particle.to_csv(particle_fname)

# df_flowline file name
flowline_fname = os.path.join(modpath_hor.dstroot,modpath_hor.schematisation_type + "_df_flowline_microbial_removal.csv")
# Save df_flowline
df_flowline.to_csv(flowline_fname)


# Create travel time plots
fpath_scatter_times_log = os.path.join(modpath_hor.dstroot,"log_travel_times_" + endpoint_id + ".png")
fpath_scatter_times = os.path.join(modpath_hor.dstroot,"travel_times_" + endpoint_id + ".png")
# # df particle
# df_particle = modpath_removal.df_particle
# time limits
tmin, tmax = 0.1, 10000.
# xcoord bounds
xmin, xmax = 0., min(50., x_point)

# Create travel time plots (lognormal)
modpath_removal.plot_age_distribution(df_particle=df_particle,
        vmin = tmin,vmax = tmax,
        fpathfig = fpath_scatter_times_log, figtext = None,x_text = 0,
        y_text = 0, lognorm = True, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')

# Create travel time plots (linear)
modpath_removal.plot_age_distribution(df_particle=df_particle,
        vmin = 0.,vmax = tmax,
        fpathfig = fpath_scatter_times, figtext = None,x_text = 0,
        y_text = 0, lognorm = False, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')

# Create concentration plots
fpath_scatter_removal_log = os.path.join(modpath_hor.dstroot,"log_removal_" + endpoint_id + ".png")

# relative conc limits
cmin, cmax = 1.e-21, 1.
# xcoord bounds
xmin, xmax = 0., min(50., x_point)

# Create travel time plots (lognormal)
modpath_removal.plot_logremoval(df_particle=df_particle,
        df_flowline=df_flowline,
        vmin = cmin,vmax = cmax,
        fpathfig = fpath_scatter_removal_log, figtext = None,x_text = 0,
        y_text = 0, lognorm = True, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')


# <codecell>
''' def test_modpath_run_phreatic_withgravelpack_traveltimes(organism_name = "MS2"):
    Phreatic scheme with gravelpack: modpath run.'''
# organism name
organism_name = "MS2"

test_phrea_gp = AW.HydroChemicalSchematisation(schematisation_type='phreatic',
                            computation_method = 'modpath',
                            what_to_export='all',
                            removal_function = 'mbo',
                            # biodegradation_sorbed_phase = False,
                            well_discharge=-319.4*24,
                            # vertical_resistance_shallow_aquifer=500,
                            porosity_vadose_zone=0.38,
                            porosity_shallow_aquifer=0.35,
                            porosity_target_aquifer=0.35,
                            recharge_rate=0.3/365.25,
                            moisture_content_vadose_zone=0.15,
                            ground_surface = 22.0,
                            thickness_vadose_zone_at_boundary=5.0,
                            thickness_shallow_aquifer=10.0,
                            thickness_target_aquifer=40.0,
                            hor_permeability_target_aquifer=35.0,
                            hor_permeability_shallow_aquifer = 0.02,
                            thickness_full_capillary_fringe=0.4,
                            redox_vadose_zone='anoxic', #'suboxic',
                            redox_shallow_aquifer='anoxic',
                            redox_target_aquifer='deeply_anoxic',
                            pH_vadose_zone=5.,
                            pH_shallow_aquifer=6.,
                            pH_target_aquifer=7.,
                            dissolved_organic_carbon_vadose_zone=10., 
                            dissolved_organic_carbon_shallow_aquifer=4., 
                            dissolved_organic_carbon_target_aquifer=2.,
                            fraction_organic_carbon_vadose_zone=0.001,
                            fraction_organic_carbon_shallow_aquifer=0.0005,
                            fraction_organic_carbon_target_aquifer=0.0005, 
                            temp_water=11.,
                            solid_density_vadose_zone= 2.650, 
                            solid_density_shallow_aquifer= 2.650, 
                            solid_density_target_aquifer= 2.650, 
                            diameter_borehole = 0.75,
                            name = organism_name,
                            diameter_filterscreen = 0.2,
                            point_input_concentration = 100.,
                            discharge_point_contamination = 100.,#made up value
                            top_clayseal = 17,
                            compute_contamination_for_date=dt.datetime.strptime('2020-01-01',"%Y-%m-%d"),
                            # Modpath grid parms
                            ncols_near_well = 20,
                            ncols_far_well = 80,
                        )

test_phrea_gp.make_dictionary()

# Remove/empty point_parameters
test_phrea_gp.point_parameters = {}

# print(test_phrea.__dict__)
modpath_phrea = mpw.ModPathWell(test_phrea_gp, #test_phrea,
                        workspace = "test5_phrea_gp",
                        modelname = "phreatic",
                        bound_left = "xmin",
                        bound_right = "xmax")
# print(modpath_phrea.__dict__)
# Run phreatic schematisation
modpath_phrea.run_model(run_mfmodel = True,
                    run_mpmodel = True)

# Create travel time plots
fpath_scatter_times_log = os.path.join(modpath_phrea.dstroot,"log_travel_times_test.png")
fpath_scatter_times = os.path.join(modpath_phrea.dstroot,"travel_times_test.png")
# df particle
df_particle = modpath_phrea.df_particle
# time limits
tmin, tmax = 0.1, 10000.
# xcoord bounds
xmin, xmax = 0., 50.

# Create travel time plots (lognormal)
modpath_phrea.plot_pathtimes(df_particle = df_particle, 
        vmin = tmin,vmax = tmax,
        fpathfig = fpath_scatter_times_log, figtext = None,x_text = 0,
        y_text = 0, lognorm = True, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')

# Create travel time plots (linear)
modpath_phrea.plot_pathtimes(df_particle = df_particle, 
        vmin = 0.,vmax = tmax,
        fpathfig = fpath_scatter_times, figtext = None,x_text = 0,
        y_text = 0, lognorm = False, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')

# <codecell>
#%%
'''def test_modpath_run_phreatic_withgravelpack_removal(organism_name = "MS2"):
    Phreatic scheme with gravelpack: modpath run.'''
# organism name
organism_name = "MS2"

# @Steven: code met plots e.d. graag elders.
# @Steven: Voeg assert toe in relatie tot final concentration == value X....

test_phrea_gp = AW.HydroChemicalSchematisation(schematisation_type='phreatic',
                            computation_method = 'modpath',
                            what_to_export='all',
                            removal_function = 'mbo',
                            # biodegradation_sorbed_phase = False,
                            well_discharge=-319.4*24,
                            # vertical_resistance_shallow_aquifer=500,
                            porosity_vadose_zone=0.38,
                            porosity_shallow_aquifer=0.35,
                            porosity_target_aquifer=0.35,
                            recharge_rate=0.3/365.25,
                            moisture_content_vadose_zone=0.15,
                            ground_surface = 22.0,
                            thickness_vadose_zone_at_boundary=5.0,
                            thickness_shallow_aquifer=10.0,
                            thickness_target_aquifer=40.0,
                            hor_permeability_target_aquifer=35.0,
                            hor_permeability_shallow_aquifer = 0.02,
                            thickness_full_capillary_fringe=0.4,
                            redox_vadose_zone='anoxic', #'suboxic',
                            redox_shallow_aquifer='anoxic',
                            redox_target_aquifer='deeply_anoxic',
                            pH_vadose_zone=5.,
                            pH_shallow_aquifer=6.,
                            pH_target_aquifer=7.,
                            dissolved_organic_carbon_vadose_zone=10., 
                            dissolved_organic_carbon_shallow_aquifer=4., 
                            dissolved_organic_carbon_target_aquifer=2.,
                            fraction_organic_carbon_vadose_zone=0.001,
                            fraction_organic_carbon_shallow_aquifer=0.0005,
                            fraction_organic_carbon_target_aquifer=0.0005, 
                            temp_water=11.,
                            solid_density_vadose_zone= 2.650, 
                            solid_density_shallow_aquifer= 2.650, 
                            solid_density_target_aquifer= 2.650, 
                            diameter_borehole = 0.75,
                            name = organism_name,
                            diameter_filterscreen = 0.2,
                            point_input_concentration = 100.,
                            discharge_point_contamination = 100.,#made up value
                            top_clayseal = 17,
                            compute_contamination_for_date=dt.datetime.strptime('2020-01-01',"%Y-%m-%d"),
                            # Modpath grid parms
                            ncols_near_well = 20,
                            ncols_far_well = 80,
                        )

test_phrea_gp.make_dictionary()

# Remove/empty point_parameters
test_phrea_gp.point_parameters = {}

# print(test_phrea.__dict__)
modpath_phrea = mpw.ModPathWell(test_phrea_gp, #test_phrea,
                        workspace = os.path.join(path,"test6_phrea_gp_removal"),
                        modelname = "phreatic",
                        bound_left = "xmin",
                        bound_right = "xmax")
# print(modpath_phrea.__dict__)
# Run phreatic schematisation
modpath_phrea.run_model(run_mfmodel = True,
                    run_mpmodel = True)

# microbial removal properties
# organism_name = 'MS2'
alpha0 = {"suboxic": 1.e-3, "anoxic": 1.e-5, "deeply_anoxic": 1.e-5}
pH0 = {"suboxic": 6.6, "anoxic": 6.8, "deeply_anoxic": 6.8}
organism_diam =  2.33e-8
mu1 = {"suboxic": 0.149,"anoxic": 0.023,"deeply_anoxic": 0.023}

removal_parameters = {organism_name: 
                {"organism_name": organism_name,
                    "alpha0": alpha0,
                    "pH0": pH0,
                    "organism_diam": organism_diam,
                    "mu1": mu1
                }
            }
# Removal parameters organism
rem_parms = removal_parameters[organism_name]

# Calculate advective microbial removal
modpath_removal = TR.Transport(modpath_phrea,
                        organism = organism_name,
                        alpha0_suboxic = rem_parms["alpha0"]["suboxic"],
                        alpha0_anoxic = rem_parms["alpha0"]["anoxic"],
                        alpha0_deeply_anoxic =rem_parms["alpha0"]["deeply_anoxic"],
                        pH0_suboxic =rem_parms["pH0"]["suboxic"],
                        pH0_anoxic =rem_parms["pH0"]["anoxic"],
                        pH0_deeply_anoxic =rem_parms["pH0"]["deeply_anoxic"],
                        mu1_suboxic = rem_parms["mu1"]["suboxic"],
                        mu1_anoxic = rem_parms["mu1"]["anoxic"],
                        mu1_deeply_anoxic = rem_parms["mu1"]["deeply_anoxic"],
                        organism_diam = rem_parms["organism_diam"]
                        )

# Calculate advective microbial removal
# Final concentration per endpoint_id
C_final = {}
for endpoint_id in modpath_phrea.schematisation_dict.get("endpoint_id"):
    df_particle, df_flowline, C_final[endpoint_id] = modpath_removal.calc_advective_microbial_removal(
                                        modpath_phrea.df_particle, modpath_phrea.df_flowline, 
                                        endpoint_id = endpoint_id,
                                        trackingdirection = modpath_phrea.trackingdirection,
                                        conc_start = 1., conc_gw = 0.)

    # Create travel time plots
    fpath_scatter_times_log = os.path.join(modpath_phrea.dstroot,"log_travel_times_" + endpoint_id + ".png")
    fpath_scatter_times = os.path.join(modpath_phrea.dstroot,"travel_times_" + endpoint_id + ".png")
    # # df particle
    # df_particle = modpath_removal.df_particle
    # time limits
    tmin, tmax = 0.1, 10000.
    # xcoord bounds
    xmin, xmax = 0., 50.

    # Create travel time plots (lognormal)
    modpath_removal.plot_age_distribution(df_particle=df_particle,
            vmin = tmin,vmax = tmax,
            fpathfig = fpath_scatter_times_log, figtext = None,x_text = 0,
            y_text = 0, lognorm = True, xmin = xmin, xmax = xmax,
            line_dist = 1, dpi = 192, trackingdirection = "forward",
            cmap = 'viridis_r')

    # Create travel time plots (linear)
    modpath_removal.plot_age_distribution(df_particle=df_particle,
            vmin = 0.,vmax = tmax,
            fpathfig = fpath_scatter_times, figtext = None,x_text = 0,
            y_text = 0, lognorm = False, xmin = xmin, xmax = xmax,
            line_dist = 1, dpi = 192, trackingdirection = "forward",
            cmap = 'viridis_r')

    # Create concentration plots
    fpath_scatter_removal_log = os.path.join(modpath_phrea.dstroot,"log_removal_" + endpoint_id + ".png")

    # relative conc limits
    cmin, cmax = 1.e-21, 1.
    # xcoord bounds
    xmin, xmax = 0., 50.

    # Create travel time plots (lognormal)
    modpath_removal.plot_logremoval(df_particle=df_particle,
            df_flowline=df_flowline,
            vmin = cmin,vmax = cmax,
            fpathfig = fpath_scatter_removal_log, figtext = None,x_text = 0,
            y_text = 0, lognorm = True, xmin = xmin, xmax = xmax,
            line_dist = 1, dpi = 192, trackingdirection = "forward",
            cmap = 'viridis_r')


# <codecell>
''' def test_modpath_run_semiconfined_nogravelpack_traveltimes(organism_name = "MS2"):
    Phreatic scheme with gravelpack: modpath run.'''

    # @Steven: test overbodig? --> plots en andere uitvoer hier weg
    # Voeg assert toe in relatie tot final concentration == value X....

test_semiconf = AW.HydroChemicalSchematisation(schematisation_type='semiconfined',
                                computation_method = 'modpath',
                                what_to_export='all',
                                removal_function = 'mbo',
                                # biodegradation_sorbed_phase = False,
                                    well_discharge=-319.4*24,
                                    # vertical_resistance_shallow_aquifer=500,
                                    porosity_vadose_zone=0.38,
                                    porosity_shallow_aquifer=0.35,
                                    porosity_target_aquifer=0.35,
                                    recharge_rate=0.3/365.25,
                                    moisture_content_vadose_zone=0.15,
                                    ground_surface = 22.0,
                                    thickness_vadose_zone_at_boundary=5.0,
                                    thickness_shallow_aquifer=10.0,
                                    thickness_target_aquifer=40.0,
                                    hor_permeability_target_aquifer=35.0,
                                    hor_permeability_shallow_aquifer = 0.02,
                                    thickness_full_capillary_fringe=0.4,
                                    redox_vadose_zone='anoxic', #'suboxic',
                                    redox_shallow_aquifer='anoxic',
                                    redox_target_aquifer='deeply_anoxic',
                                    pH_vadose_zone=5.,
                                    pH_shallow_aquifer=6.,
                                    pH_target_aquifer=7.,
                                    dissolved_organic_carbon_vadose_zone=10., 
                                    dissolved_organic_carbon_shallow_aquifer=4., 
                                    dissolved_organic_carbon_target_aquifer=2.,
                                    fraction_organic_carbon_vadose_zone=0.001,
                                    fraction_organic_carbon_shallow_aquifer=0.0005,
                                    fraction_organic_carbon_target_aquifer=0.0005, 
                                    diffuse_input_concentration = 100, #ug/L
                                    temp_water=11.,
                                    solid_density_vadose_zone= 2.650, 
                                    solid_density_shallow_aquifer= 2.650, 
                                    solid_density_target_aquifer= 2.650, 
                                    diameter_borehole = 0.75,
                                    name = organism_name,
                                    # diameter_filterscreen = 0.2,
                                    point_input_concentration = 100.,
                                    discharge_point_contamination = 100.,#made up value
                                    top_clayseal = 17,
                                    compute_contamination_for_date=dt.datetime.strptime('2020-01-01',"%Y-%m-%d"),
                                    
                                    ncols_near_well = 20,
                                    ncols_far_well = 20,
                                    nlayers_target_aquifer = 20,

                                )

test_semiconf.make_dictionary()

# Test concentration_boundary_parameters (check line 796 in ModPath_functions)
concentration_boundary_parameters = test_semiconf.recharge_parameters

# Remove/empty point_parameters
test_semiconf.point_parameters = {}

modpath_semiconf = mpw.ModPathWell(test_semiconf, # semiconf_dict_1, #test_phrea,
                        workspace = os.path.join(path,"test7_semiconf_nogp"),
                        modelname = "semi_conf_nogp",
                        bound_left = "xmin",
                        bound_right = "xmax")

# Run phreatic schematisation
modpath_semiconf.run_model(run_mfmodel = True,
                    run_mpmodel = True)

# Calculate advective microbial removal
modpath_removal = TR.Transport(modpath_semiconf,
                                        organism = organism_name,
                                        )
# modpath_removal.compute_omp_removal()
# Final concentration per endpoint_id
C_final = {}
for endpoint_id in modpath_semiconf.schematisation_dict.get("endpoint_id"):
    df_particle, df_flowline, C_final[endpoint_id] = modpath_removal.calc_advective_microbial_removal(
                                        modpath_semiconf.df_particle, modpath_semiconf.df_flowline, 
                                        endpoint_id = endpoint_id,
                                        trackingdirection = modpath_semiconf.trackingdirection,
                                        mu1 = 0.023, grainsize = 0.00025, alpha0 = 1.E-5, pH0 = 6.8,
                                        temp_water = 11., rho_water = 999.703, organism_diam = 2.33e-8,
                                        conc_start = 1., conc_gw = 0.)

# df_particle file name 
particle_fname = os.path.join(modpath_semiconf.dstroot,modpath_semiconf.schematisation_type + "_df_particle_microbial_removal.csv")
# Save df_particle 
df_particle.to_csv(particle_fname)

# df_flowline file name
flowline_fname = os.path.join(modpath_semiconf.dstroot,modpath_semiconf.schematisation_type + "_df_flowline_microbial_removal.csv")
# Save df_flowline
df_flowline.to_csv(flowline_fname)


# Create travel time plots
fpath_scatter_times_log = os.path.join(modpath_semiconf.dstroot,"log_travel_times_test.png")
fpath_scatter_times = os.path.join(modpath_semiconf.dstroot,"travel_times_test.png")
# df particle
df_particle = modpath_semiconf.df_particle
# time limits
tmin, tmax = 0.1, 10000.
# xcoord bounds
xmin, xmax = 0., 100.

# Create travel time plots (lognormal)
modpath_semiconf.plot_pathtimes(df_particle = df_particle, 
        vmin = tmin,vmax = tmax,
        fpathfig = fpath_scatter_times_log, figtext = None,x_text = 0,
        y_text = 0, lognorm = True, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')

# Create travel time plots (linear)
modpath_semiconf.plot_pathtimes(df_particle = df_particle, 
        vmin = 0.,vmax = tmax,
        fpathfig = fpath_scatter_times, figtext = None,x_text = 0,
        y_text = 0, lognorm = False, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')


#<codecell>
''' def test_travel_time_distribution_phreatic_analytical_plus_modpath(organism_name = "MS2"):
    Compare AnalyticalWell.py and ModpathWell.py travel times distribution.'''

# @ Steven: plots naar readthedocs --> niet in test toevoegen
# assert_frame_equal analytical vs Modpath df_uitvoer behouden

output_phreatic = pd.read_csv(path / 'phreatic_test_mp.csv')
output_phreatic = output_phreatic.round(7) #round to 7 digits (or any digit), keep same as for the output for the model to compare
output_phreatic.index = RangeIndex(start = 1,stop=len(output_phreatic.index)+1)

test_phrea = AW.HydroChemicalSchematisation(schematisation_type='phreatic',
                                    computation_method= 'analytical',
                                    what_to_export='all',
                                    removal_function = 'mbo',
                                    well_discharge=-319.4*24,
                                    # vertical_resistance_shallow_aquifer=500,
                                    hor_permeability_shallow_aquifer = 35.,
                                    porosity_vadose_zone=0.38,
                                    porosity_shallow_aquifer=0.35,
                                    porosity_target_aquifer=0.35,
                                    recharge_rate=0.3/365.25,
                                    moisture_content_vadose_zone=0.15,
                                    ground_surface = 22,
                                    thickness_vadose_zone_at_boundary=5,
                                    thickness_shallow_aquifer=10,
                                    thickness_target_aquifer=40,
                                    hor_permeability_target_aquifer=35,
                                    # KD=1400,
                                    ncols_near_well = 20,
                                    ncols_far_well = 100,
                                    
                                    thickness_full_capillary_fringe=0.4,
                                    temp_water=11,
                                    solid_density_vadose_zone= 2.650,
                                    solid_density_shallow_aquifer= 2.650,
                                    solid_density_target_aquifer= 2.650,
                                    diameter_borehole = 0.75,
                                    name=organism_name
                                    )

# AnalyticalWell object
well1_an = AW.AnalyticalWell(test_phrea)
well1_an.phreatic()
df_particle_an = well1_an.df_particle
df_particle_an = df_particle_an.round(7)

# ModPath well object
well1_mp = mpw.ModPathWell(test_phrea, #test_phrea,
                        workspace = os.path.join(path,"test11_phrea"),
                        modelname = "phreatic",
                        bound_left = "xmin",
                        bound_right = "xmax")

# Run phreatic schematisation
well1_mp.run_model(run_mfmodel = True,
                    run_mpmodel = True)

df_particle_mp = well1_mp.df_particle
# Obtain "flowline_id" from current index ;Add RangeIndex
df_particle_mp["flowline_id"] = df_particle_mp.index
df_particle_mp.index = RangeIndex(start = 1,stop=len(df_particle_mp.index)+1)
# df_particle_mp = df_particle_mp[["total_travel_time", "travel_time_unsaturated",
#                  "travel_time_shallow_aquifer", "travel_time_target_aquifer",
#                  "radial_distance", ]]
df_particle_mp = df_particle_mp.round(7)

# Export output of analytical and modpath calculations

# df_particle file name (analytical well data)
particle_fname_an = os.path.join(well1_mp.dstroot,well1_mp.schematisation_type + "_df_particle_analytical.csv")
# Save df_particle 
df_particle_an.to_csv(particle_fname_an)

# df_particle file name 
particle_fname_mp = os.path.join(well1_mp.dstroot,well1_mp.schematisation_type + "_df_particle_modpath.csv")
# Save df_particle 
df_particle_mp.to_csv(particle_fname_mp)


# Columns in summary dataframe traveltimes
summary_columns = output_phreatic.columns
# flowline indices
flowline_ids_an = list(df_particle_an.loc[:,"flowline_id"].unique())
# Zones to compare
zones = ["vadose_zone","shallow_aquifer","target_aquifer"]

# Summary traveltimes (analytical)
summary_traveltimes_an = pd.DataFrame(index = flowline_ids_an,
                                    columns = summary_columns)
# Fill summary df         
for fid in flowline_ids_an:
    # Total traveltime
    summary_traveltimes_an.loc[fid,"total_travel_time"] = \
                            df_particle_an.loc[df_particle_an["flowline_id"] == fid,:].sort_values(by="total_travel_time", 
                                    ascending = True).loc[:,"total_travel_time"].iloc[-1]
    # Starting location
    summary_traveltimes_an.loc[fid,"xcoord"] = \
                    df_particle_an.loc[df_particle_an["flowline_id"] == fid,:].sort_values(by="total_travel_time", 
                            ascending = True).loc[:,"xcoord"].iloc[0]
    for iZone in zones:
        # Travel time per zone
        summary_traveltimes_an.loc[fid,"travel_time_" + iZone] = df_particle_an.loc[(df_particle_an["flowline_id"] == fid) & (df_particle_an["zone"] == iZone),"travel_time"].values[0]

# Summary traveltimes (Numerical / modpath)
# flowline indices (modpath)
flowline_ids_mp = list(df_particle_mp.loc[:,"flowline_id"].unique())
summary_traveltimes_mp = pd.DataFrame(index = flowline_ids_mp,
                                    columns = summary_columns)

# Fill summary df         
for fid in flowline_ids_mp:
    # Total traveltime
    summary_traveltimes_mp.loc[fid,"total_travel_time"] = \
                            df_particle_mp.loc[df_particle_mp["flowline_id"] == fid,:].sort_values(by="total_travel_time", 
                                    ascending = True).loc[:,"total_travel_time"].iloc[-1]
    # Starting location
    summary_traveltimes_mp.loc[fid,"xcoord"] = \
                    df_particle_mp.loc[df_particle_mp["flowline_id"] == fid,:].sort_values(by="total_travel_time", 
                            ascending = True).loc[:,"xcoord"].iloc[0]
    
    ## Travel time per zone ##
    # Vadose zone
    summary_traveltimes_mp.loc[fid,"travel_time_vadose_zone"] = abs(df_particle_mp.loc[(df_particle_mp["flowline_id"] == fid) & (df_particle_mp["zone"] == "shallow_aquifer"),"total_travel_time"].values.min() - \
                                                                df_particle_mp.loc[(df_particle_mp["flowline_id"] == fid) & (df_particle_mp["zone"] == "vadose_zone"),"total_travel_time"].values.min())
    # Shallow aquifer
    summary_traveltimes_mp.loc[fid,"travel_time_shallow_aquifer"] = abs(df_particle_mp.loc[(df_particle_mp["flowline_id"] == fid) & (df_particle_mp["zone"] == "target_aquifer"),"total_travel_time"].values.min() - \
                                                                df_particle_mp.loc[(df_particle_mp["flowline_id"] == fid) & (df_particle_mp["zone"] == "shallow_aquifer"),"total_travel_time"].values.min())
    # Target aquifer
    summary_traveltimes_mp.loc[fid,"travel_time_target_aquifer"] = abs(df_particle_mp.loc[(df_particle_mp["flowline_id"] == fid) & (df_particle_mp["zone"] == "well1"),"total_travel_time"].values.min() - \
                                                                df_particle_mp.loc[(df_particle_mp["flowline_id"] == fid) & (df_particle_mp["zone"] == "target_aquifer"),"total_travel_time"].values.min())

# df_particle file name (analytical well data)
summary_fname_an = os.path.join(well1_mp.dstroot,well1_mp.schematisation_type + "_summary_traveltimes_analytical.csv")
# Save df_particle 
summary_traveltimes_an.to_csv(summary_fname_an)

# df_particle file name 
summary_fname_mp = os.path.join(well1_mp.dstroot,well1_mp.schematisation_type + "_summary_traveltimes_modpath.csv")
# Save df_particle 
summary_traveltimes_mp.to_csv(summary_fname_mp)

# Create traveltime distribution plot using Substance Transport class
modpath_removal = TR.Transport(well1_mp,
                        organism = organism_name)

modpath_removal.plot_travel_time_distribution(modpath_removal.df_particle, times_col = "total_travel_time",
                                    distance_col = "xcoord", index_col = "flowline_id",
                                    fpath_fig = None)

## analytical solution ##
# Distance points
distance_points_an = np.empty((len(flowline_ids_an)), dtype = 'float')
# Time points
time_points_an = np.empty((len(flowline_ids_an)), dtype = 'float')

for idx, fid in enumerate(flowline_ids_an):

    # Fill distance_points array
    distance_points_an[idx] = summary_traveltimes_an.loc[summary_traveltimes_an.index == fid, ["xcoord","total_travel_time"]].sort_values(
                                by = "total_travel_time", ascending = True).iloc[-1,0]

    # Fill time_points array
    time_points_an[idx] = summary_traveltimes_an.loc[summary_traveltimes_an.index == fid, ["xcoord","total_travel_time"]].sort_values(
                                by = "total_travel_time", ascending = True).iloc[-1,1]

## modpath solution ##
# Distance points
distance_points_mp = np.empty((len(flowline_ids_mp)), dtype = 'float')
# Time points
time_points_mp = np.empty((len(flowline_ids_mp)), dtype = 'float')

for idx, fid in enumerate(flowline_ids_mp):

    # Fill distance_points array
    distance_points_mp[idx] = summary_traveltimes_mp.loc[summary_traveltimes_mp.index == fid, ["xcoord","total_travel_time"]].sort_values(
                                by = "total_travel_time", ascending = True).iloc[-1,0]
        
    # Fill time_points array
    time_points_mp[idx] = summary_traveltimes_mp.loc[summary_traveltimes_mp.index == fid, ["xcoord","total_travel_time"]].sort_values(
                                by = "total_travel_time", ascending = True).iloc[-1,1]


# Create travel time distribution plot
fig, ax = plt.subplots(figsize= (10,10),dpi=300)

# Plot time-radius plot
plt.plot(distance_points_an, time_points_an, lw = 0., marker = '.')  # analytical
plt.plot(distance_points_mp, time_points_mp, lw = 0.2)  # modpath
plt.xlabel("Radial distance (m)")
plt.ylabel("Travel time (days)")

# travel distribution plot (analytic vs numeric)
fpath_traveltime_plot = os.path.join(well1_mp.dstroot,well1_mp.schematisation_type + "_traveltimes_modpath.png")
fig.savefig(fpath_traveltime_plot)


# Create travel time plots
fpath_scatter_times_log = os.path.join(well1_mp.dstroot,"log_travel_times_test.png")
fpath_scatter_times = os.path.join(well1_mp.dstroot,"travel_times_test.png")
# df particle
df_particle = well1_mp.df_particle
# time limits
tmin, tmax = 0.1, 10000.
# xcoord bounds
xmin, xmax = 0., 50.

# Create travel time plots (lognormal)
well1_mp.plot_pathtimes(df_particle = df_particle, 
        vmin = tmin,vmax = tmax,
        fpathfig = fpath_scatter_times_log, figtext = None,x_text = 0,
        y_text = 0, lognorm = True, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')

# Create travel time plots (linear)
well1_mp.plot_pathtimes(df_particle = df_particle, 
        vmin = 0.,vmax = tmax,
        fpathfig = fpath_scatter_times, figtext = None,x_text = 0,
        y_text = 0, lognorm = False, xmin = xmin, xmax = xmax,
        line_dist = 1, dpi = 192, trackingdirection = "forward",
        cmap = 'viridis_r')


#<markdowncell>
# '''
# def test_omp_removal_modpath_input(substance_name = 'AMPA'):
#     calculate the removal of a default substance using ModPathWell class.'''

# Lets start with a simple example defining a HydroChemicalSchematisation object for a phreatic aquifer:

#<codecell>
phreatic_schematisation = AW.HydroChemicalSchematisation(schematisation_type='phreatic',
                                                    computation_method = 'modpath',
                                                    removal_function = 'omp',
                                                    well_discharge=-7500, #m3/day
                                                    recharge_rate=0.0008, #m/day
                                                    thickness_vadose_zone_at_boundary=5, #m
                                                    thickness_shallow_aquifer=10,  #m
                                                    thickness_target_aquifer=40, #m
                                                    hor_permeability_target_aquifer=35, #m/day
                                                    redox_vadose_zone='anoxic',
                                                    redox_shallow_aquifer='anoxic',
                                                    redox_target_aquifer='deeply_anoxic',
                                                    pH_target_aquifer=7.,
                                                    temp_water=11.,
                                                    name='benzene',
                                                    diffuse_input_concentration = 100, #ug/L
                                                    )

#<markdowncell>
# ## The parameters from the HydroChemicalSchematisation class are added as attributes to
# ## the class and can be accessed for example:

# Then, we create a ModpathWell object for the HydroChemicalSchematisation object that we just made.
# The ModpathWell object requires a dictionary of the subsurface schematisation and a set of boundary conditions
# the numerical model has to abide by in calculating flow velocity and direction of flow.

#<codecell>
phreatic_schematisation.make_dictionary()

#<markdowncell>
# ## Step 2: Run the ModpathWell class
# ## =====================================
# Next we create an ModpathWell object for the HydroChemicalSchematisation object we just made.
# The data files will be stored in location workspace using a given modelname.

#<codecell>
modpath_phrea = mpw.ModPathWell(phreatic_schematisation,
                            workspace = os.path.join(path,"test7_omp_removal"),
                            modelname = "phreatic")

#<markdowncell>
# Now we run the Modpath model, which numerically calculates the flow in the subsurface using the 
# 'schematisation' dictionary stored in the HydroChemicalSchematisation object. By default the model will
# calculate both the hydraulic head distribution (using modflow: 'run_mfmodel' = True) and
# the particle pathlines [X,Y,Z,T-data] (using modpath: 'run_mpmodel' = True) with which OMP removal
# or microbial organism ('mbo') removal is later calculated.

#<codecell>
modpath_phrea.run_model(run_mfmodel = True,
                    run_mpmodel = True)

#<markdowncell>
# ## Step 3: Collect removal parameters
# ## ===========================================

# Step 3a: View the Substance class (Optional)
# ============================================
# You can retrieve the default removal parameters used to calculate the removal of organic micropollutants [OMP] 
# in the SubstanceTransport class. The data are stored in a dictionary

#<codecell>
test_substance = TR.Substance(substance_name='benzene')
test_substance.substance_dict

# ## Step 4: Run the SubstanceTransport class
# ## ========================================
# To calculate the removal and the steady-state concentration in each zone (analytical solution) or per particle node (modpath), create a concentration
# object by running the SubstanceTransport class with the phreatic_well object and specifying
# the OMP or microbial organism (mbo) of interest. 
# The type of removal is defined using the option 'removal_function: 'omp' or 'mbo'
# All required parameters for removal are stored as 'removal_parameters'.

# Step 4b: Calculate the OMP removal
# ========================================
# As example, we take the default removal parameters for the substances 'AMPA'.
# Note: For OMP you will have to specify values relevant for substances (e.g. half-life, pKa, log_Koc).
# Any/all default values will be stored and used in the calculation of the removal. 
# Note that by default the class expects the removal of microbial organisms copied from removal_function 
# entered in modpath_phrea. We have to explicitly enter the removal_function below for removal op substances.
# removal_function == 'omp'

# substance (AMPA)

#<codecell>
substance_name = 'AMPA'

#<markdowncell>
# Calculate removal of organic micro-pollutants (removal_function = 'omp')

#<codecell>
modpath_removal = TR.Transport(well = modpath_phrea,
                        substance = substance_name,
                        partition_coefficient_water_organic_carbon=None,
                        dissociation_constant=None,
                        halflife_suboxic=None,
                        halflife_anoxic=None,
                        halflife_deeply_anoxic=None,
                        removal_function = 'omp',
                        )

#<markdowncell>
# View the updated removal_parameters dictionary from the SubstanceTransport object

#<codecell>
modpath_removal.removal_parameters

#<markdowncell>
# We compute the removal by running the 'compute_omp_removal' function

#<codecell>
modpath_removal.compute_omp_removal()

#<markdowncell>
# Once the removal has been calculated, you can view the steady-state concentration
# and breakthrough time per zone for the OMP in the df_particle:

#<codecell>
modpath_removal.df_particle.loc[:,['zone', 'steady_state_concentration', 'travel_time']].head(4)

#<markdowncell>
# View the steady-state concentration of the flowline or the steady-state
# contribution of the flowline to the concentration in the well

#<codecell>
modpath_removal.df_flowline.loc[:,['breakthrough_concentration', 'total_breakthrough_travel_time']].head(5)

#<markdowncell>
# Plot the breakthrough curve at the well over time:

#<codecell>
benzene_plot = modpath_removal.plot_concentration(ylim=[0,10 ])

# image:: benzene_plot.png
#<markdowncell>
# You can also compute the removal for a different OMP of interest:

# * OMP-X: a ficticous OMP with no degradation or sorption
# * AMPA
# * benzo(a)pyrene

# To do so you can use the original schematisation, but specify a different OMP when you create
# the SubstanceTransport object.

#<codecell>
phreatic_concentration = TR.Transport(modpath_phrea, substance = 'OMP-X')
phreatic_concentration.compute_omp_removal()
omp_x_plot = phreatic_concentration.plot_concentration(ylim=[0,100 ])

# image:: omp_x_plot.png 

phreatic_concentration = TR.Transport(modpath_phrea, substance = 'benzo(a)pyrene')
phreatic_concentration.compute_omp_removal()
benzo_plot = phreatic_concentration.plot_concentration(ylim=[0,1])

# image:: benzo_plot.png

phreatic_concentration = TR.Transport(modpath_phrea, substance = 'AMPA')
phreatic_concentration.compute_omp_removal()
ampa_plot = phreatic_concentration.plot_concentration( ylim=[0,1])

# image:: ampa_plot.png

#<markdowncell>
# Other examples in the Bas_tutorial.py file are:

# * diffuse/point source example for phreatic 
# * semiconfined example

# <codecell>
