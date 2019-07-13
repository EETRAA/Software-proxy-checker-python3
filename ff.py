# encoding: utf-8
import sys
import re
import time

time1=time.time()
#ip_parser_func
def ip_parser(input_file_name,output_file_name):
  input_file = open(input_file_name)
  ip_list=[]
  
  for each in input_file:
    ip=re.findall(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):[0-9]{1,5}',str(each),re.S)
    #print(ip)#debug
    ip_list.append(ip)#append_new_item_to_ip_lsit
    #ip_list=list(set(ip_list))_first_try_failed_
  output_file = open(output_file_name, "a")#write_the_ip_list
  for each in ip_list:
    #print (each)#debug
    #if each == []:
      #print("eoooooooooooo")#debug
    if each != []:
      output_file.write(str(each) + "\n")
  #close_all_files
  output_file.close()
  input_file.close()
  print ("--ip_parser_done--")
#main_starts_here################
if __name__ == '__main__':
  input_file_name = "input_file.txt"
  output_file_name = "output_file.txt"
  ip_parser(input_file_name,output_file_name)
  time2 = time.time()
  print (u'Time cost' + str(time2 - time1) + 's')