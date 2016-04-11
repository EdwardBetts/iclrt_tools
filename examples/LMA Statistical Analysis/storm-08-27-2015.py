#!/usr/bin/env python

import iclrt_tools.lma.analysis.storm_analysis as st

# File names for first and second part of storm analysis
file1 = '/home/jaime/Documents/ResearchTopics/Publications/LightningEvolution/Storm-08-27-2015/LMA/ChargeAnalysis-1of2-exported.csv'
file2 = '/home/jaime/Documents/ResearchTopics/Publications/LightningEvolution/Storm-08-27-2015/LMA/ChargeAnalysis-2of2-exported.csv'

dates = ['08/27/2015', '08/28/2015']

file_name = '/home/jaime/Documents/ResearchTopics/Publications/LightningEvolution/Storm-08-27-2015/LMA Analysis 08272015.csv'

storm_lma = st.Storm.from_lma_files([file1, file2], dates)
storm_ods = st.Storm.from_ods_file(file_name)

# Get flash numbers for all ODS flashes
results = storm_lma.get_analyzed_flash_numbers(storm_ods)


# storm_lma.plot_charge_region(charge='positive', show_plot=True)
# storm_lma.plot_charge_region(charge='negative', show_plot=True)
# storm_lma.plot_all_charge_regions(show_plot=True)

# storm_lma.get_storm_summary(charge='positive')
# storm_lma.get_storm_summary(charge='negative')
# storm_lma.get_storm_summary(charge='other')
# storm_ods.get_storm_summary(flash_types=['IC'])

# storm_ods.get_flash_rate(category='CG')
# storm_ods.get_flash_rate(category='IC')
# storm_lma.plot_interval(path='/home/jaime/Documents/ResearchTopics/Publications/LightningEvolution/Storm-08-27-2015/Figures/Statistical Analysis/')

# storm_lma.measure_flash_area('/home/jaime/Documents/ResearchTopics/Publications/LightningEvolution/Storm-08-27-2015/Statistical Analysis/storm-08-27-2015_flash_areas.csv')