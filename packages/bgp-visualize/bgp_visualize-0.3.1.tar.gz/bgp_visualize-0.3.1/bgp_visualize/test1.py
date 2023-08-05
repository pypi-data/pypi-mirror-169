#!/usr/bin/python
__author__ = "Bassem Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import bgp_visualize_asn

# provide a country code as an argument
country_1 = bgp_visualize_asn.bgp_visualize(country="pk")

# you can also choose the "dark" theme for the graph
country_2 = bgp_visualize_asn.bgp_visualize(country="sa", dark=True)
country_1.Draw()
country_2.Draw()

# you can also provide a list of bgp autonomous systems to visualize
Operators_in_EGYPT = bgp_visualize_asn.bgp_visualize(asns=[8452, 24835, 36992, 24863], dark=True)
Operators_in_EGYPT.Draw()
