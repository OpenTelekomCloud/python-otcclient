#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of OTC Tool released under MIT license.
# Copyright (C) 2016 T-systems Kurt Garloff, Zsolt Nagy

from otcclient.core.OtcConfig import OtcConfig 
from otcclient.utils import utils_http, utils_templates

from otcclient.core.otcpluginbase import otcpluginbase
from otcclient.core.pluginmanager import getplugin
   
from otcclient.core.argmanager import arg, otcfunc 

import string
 
class rds(otcpluginbase):
    ar = {}    
    
    @staticmethod
    def otcOutputHandler(): 
        return getplugin(OtcConfig.OUTPUT_FORMAT)
 
    def otctype(self):
        return "func" 

    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="create rds cluster",
             examples = [
                 {'otc rds create_cluster --subnet-id  1111111-1111-1111-1111-a96f27f31111 --vpc-name MYVPC --group-names MYSECGROUP --cluster-name TEST --admin-pass Test1234+'}
                 ],
             args = [ 
                arg(
                    '--cluster-name',
                    dest='CLUSTER',
                    help='create cluster'
                )
                ]                
             )

    def create_cluster():               
        url = "https://" + OtcConfig.DEFAULT_HOST + "/rds/v1/"+ OtcConfig.PROJECT_ID +"/instances"
        url = string.replace(url, 'iam', 'rds')

        #vpc_id
        if not (OtcConfig.VPCNAME is None):
            getplugin("ecs").convertVPCNameToId()
          
        #network_id
        if not OtcConfig.SUBNETNAME is None:
            getplugin("ecs").convertSUBNETNameToId()

        if (not (OtcConfig.SECUGROUPNAME is None)):
            getplugin("ecs").convertSECUGROUPNameToId() 

        if not OtcConfig.SUBNETNAME is None:
            ecs.convertSUBNETNameToId()

        if (OtcConfig.DBTYPE is None):
            OtcConfig.DBTYPE = "MySQL"

        if (OtcConfig.DBVERSION is None):
            OtcConfig.DBVERSION = "5.7.20"

        
        REQ_CREATE_CLUSTER=utils_templates.create_request("create_cluster")

        ret = utils_http.post(url, REQ_CREATE_CLUSTER)
        print REQ_CREATE_CLUSTER
        print (url)
        print (ret)        
        rds.otcOutputHandler().print_output(ret, mainkey = "") 


    @staticmethod
    def add():
        # TODO: NOT implemented         
        ret = utils_templates.create_request("as_modify")
        return ret


    @staticmethod
    @otcfunc(plugin_name=__name__,
             desc="Description of all DB instances",
             examples=[
                       {"List DB instances":"otc rds describe_db_instances"}
                       ],
             args = [ ]
             )
    def describe_db_instances():
        url = "https://" + OtcConfig.DEFAULT_HOST + "/rds/v1/"+ OtcConfig.PROJECT_ID + "/instances"
        ret = utils_http.get(url)
        return ret
