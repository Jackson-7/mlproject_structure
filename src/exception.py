import sys
import logging

def error_message_detail(error,error_detail:sys):
    ''' 
    We are not intrested in the first 2 variables/details we are intrested in the 3rd variable 
    'exc_tb'. This variable will tell us where and in which file the error has occured and all 
    imp infos. 
    '''
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
    
    
#if __name__=="__main__":
#    try:
#        a=1/0
#    except Exception as e:
#        logging.info("Test error: %s",str(e))
#        raise CustomException(e,sys)