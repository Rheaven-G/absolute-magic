#!/usr/bin/env python

import os
import sys
import shutil
import json

class AbsoluteMagic:
    def __init__( self,
                  path      :str    =None,
                  platform      :str    ='darwin' ):
        self.PATH = path
        self.config, self.settings = self.load()


        self.load()
        self.start()
        self.update()
        self.end()

    def load( self ) -> tuple[dict, dict]:
        user_config_file_name = r'user.config'

        if not os.path.isfile( os.path.join( self.PATH, user_config_file_name )):
            print( 'Config does not exist. Creating one...' )

            shutil.copyfile( os.path.join( r'default.config' ),
                             os.path.join( self.PATH, user_config_file_name ) )

        with open( os.path.join(self.PATH, user_config_file_name),'r' ) as f:
            config = json.load( f )


        return config








if __name__ == '__main__':
    user_home = os.path.expanduser( '~' )
    am_working_directory = os.path.join( user_home, 'Documents', 'AbsoluteMagic' )

    am = AbsoluteMagic(
            path =am_working_directory,
            platform=sys.platform )