# Complete booking flow

####Login with registered credential - Create on_start task name login_demotour with post request
    ##verify through resp.text that user is on find flight page with post request
####Click continue with default value - task name find_flight with post request- give weigtage 4
   ##verify through resp.text that user is on select flight page with post request 
####Click continue with default value - task name select_flight with post request-give weigtage 2
   ##verify through resp.text that user is on book flight page with post request
####Fill form with data & click secure purchase- task name book_flight with post request-give weigtage 1
   ##verify through resp.text that user gets booking confirmation with post request
#Once script is verified, modify script to take 5 registered users
#Run script with --logfile option to generate log file
#Run test with 5 unique users
