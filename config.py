"""
Module config
"""
import datetime
import logging
import os


class Config:
    """
    Class Config

    For project settings
    """

    def __init__(self):
        """
        Constructor
        """

        '''
        Date Stamp
        '''
        now = datetime.datetime.now()
        self.stamp: str = now.strftime('%Y-%m-%d')
        logging.info(self.stamp)

        '''
        Keys
        '''
        self.architecture = 'arc-state-space-sandbox'
        self.s3_parameters_key = 's3_parameters.yaml'
        self.arguments_key = f'architectures/{self.architecture}/arguments.json'
        self.metadata = f'architectures/{self.architecture}/metadata.json'

        '''
        Project Metadata
        '''
        self.project_tag = 'hydrography'
        self.project_key_name = 'HydrographyProject'

        '''
        Local Paths
        '''
        sections = ['assets', self.architecture, self.stamp]
        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')
        self.assets_ = os.path.join(self.warehouse, *sections)

        '''
        Cloud
        '''
        self.prefix = '/'.join(sections)
