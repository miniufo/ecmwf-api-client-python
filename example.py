#!/usr/bin/env python
#
# (C) Copyright 2012-2013 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0. 
# In applying this licence, ECMWF does not waive the privileges and immunities 
# granted to it by virtue of its status as an intergovernmental organisation nor
# does it submit to any jurisdiction.
#

from ecmwfapi import ECMWFDataServer

# To run this example, you need an API key 
# available from https://api.ecmwf.int/v1/key/

server=ECMWFDataServer()
server.retrieve({
    "dataset"  : "interim",
    'step'     : '0',
    'levtype'  : 'sfc',
    'date'     : '20071001',
    'time'     : '00:00:00/06:00:00/12:00:00/18:00:00',
    'type'     : 'an',
    'param'    : 'z/msl/10u/10v/sp/sst',
    'area'     : '84/81/-15/222',
    'grid'     : '0.75/0.75',
    'target'   : 'D:/data.grb'
})
