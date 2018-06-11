#
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use self file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

 
from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util 




class options(object): 
    """ options class provides a way to specify additional arguments required while fetching the resource.
    """
    _pageno=0
    _pagesize=0
    _detailview=False
    _compression=""
    _action=""
    _args=""
    _filter=""
    _count=False
    
    
    def __init__(self):
        """ options class constructor.
        """
        self._compression =  True
        self._detailview = True
        self._pageno = 0
        self._pagesize = 0
        self._action = None
        self._filter = None
        self._count = False
    
    @property
    def pageno(self): 
        return self._pageno
    
    @pageno.setter
    def pageno(self, no):
        """ sets page number.
        
        @param no page number.
        """
        self._pageno = no

    @property
    def pagesize(self): 
        return self._pagesize;


    @pagesize.setter
    def pagesize(self, size): 
        """ sets the _pagesize.
        
        @param size number of pages to be retrieved.
        """
        self._pagesize = size

    
    
    # @return _action.
    @property
    def action(self): 
        return self._action
    
    
    @action.setter
    def action(self, action): 
        """ sets the _action to be performed.
        
        @param _action _action.
        """
        self._action = action

    @property
    def compression(self): 
        return self._compression

    @compression.setter
    def compression(self, flag): 
        self._compression = flag
    
    
    @property
    def detailview(self): 
        """ @return detail view.
        """
        return self._detailview
    
    
    @detailview.setter
    def detailview(self, flag): 
        """ sets the detail view. if detail view is needed set it to true.
        
        @param flag
        """
        self._detailview = flag
    
    
    @property
    def count(self): 
        """  @return _count.
        """
        return self._count
    
    
    @count.setter
    def count(self, flag): 
        """ sets the _count. 
        
        @param flag set self to true to find the number of resources of a type configured on NS
        """
        self._count = flag
    
    
    @property
    def args(self):
        """ returns args field
        """
        return self._args
    
    
    @args.setter
    def args(self, args): 
        """ sets _args field.
        
        @param _args optional _args required for any operation. self is in json format.
        """
        self._args = args
    
 
    @property
    def filter(self):
        """ @return returns _filter.
        """
        return self._filter

    
    @filter.setter
    def filter(self, filter_str_array):
        """ sets _filter field.
        
        @param _filter set self with the _filter string to perform filtered get operation. 
        
        Set the _filter parameters in filtervalue object which is then converted to json string.
        """
        try:
            if type(filter_str_array) is list :
                filter_str = ""
                for i in filter_str_array:
                    if (filter_str):
                        filter_str = filter_str + ","
                    if not filter_str :
                        filter_str = i.name + ":" + nitro_util.encode(i.value)
                    else:
                        filter_str = filter_str + i.name + ":" + nitro_util.encode(i.value)
                self._filter = filter_str
            else :
                filter_str_array = filter_str_array.split(':') 
                self._filter = filter_str_array[0] + ":" + filter_str_array[1]
        except Exception as e:
            raise e           
    

    def to_string(self):
        """ constructs a string for options object.
        
        @return String to be concatenated to the URL.
        """
        try: 
            options_str = ""
            if (self._pageno > 0): 
                options_str = "pageno="+self._pageno
            if (self._pagesize > 0): 
                if (len(options_str) > 0):
                    options_str = options_str + "&"
                options_str = options_str +"pagesize="+self._pagesize
        
            if self._detailview is True: 
                if options_str :
                    options_str = options_str + "&"            
                options_str = options_str +"view=detail"
        
            if self._count is True : 
                if options_str :
                    options_str = options_str + "&"            
                options_str = options_str +"count=yes"
        
            if self._args :
                if options_str:
                    options_str = options_str + "&"
                options_str = options_str+"args="+self._args

            if self._filter :
                if options_str :
                    options_str = options_str + "&"
                options_str = options_str+"filter="+self._filter
            return options_str
        except Exception as e:
            raise e

