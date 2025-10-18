import argparse
import json
import os

from sys import exit

print("\n Converter YouTube Live-Chat JSON file to Text file - ver. 1.00")
print(" Copyright (c) 2025 by Sebastian Stybel, www.BONO.Edu.PL")
print("--------------------------------------------------------------------\n")

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--json", help="Input JSON Chat file or 'auto' to select first JSON file in current directory")
parser.add_argument("--output", help="Output text Chat file or 'auto' to create output file with same name as input file and add .txt extension")
parser.add_argument("--print", help="Print Chat messages to console", action="store_true")
parser.add_argument("-h", "--help", help="Show this help message and exit", action="store_true")
args = parser.parse_args()

if (args.help):
   parser.print_help()
   exit(0)

if (args.json):
   fn_json = args.json
   fn_json = fn_json.lower()
   
   if fn_json == "auto":
      files_in_dir = os.listdir('.')
      json_files = [f for f in files_in_dir if f.endswith('.json')]
      if len(json_files) == 0:
         print("No JSON Chat files found in current directory")
         exit(0)
      fn_json = json_files[0]
      print(f"Auto-selected JSON Chat file: {fn_json}")
   else:
      if not os.path.isfile(fn_json):
         print(f"JSON Chat file not found: {fn_json}")
         exit(0)
      else:
         print(f"Using specified JSON Chat file: {fn_json}")    
else:
   print("No JSON Chat file specified with --json. Use --help argument to show help information.")
   exit(0)

if (args.output):
   fn_output = args.output
   fn_output = fn_output.lower()
   
   if fn_output == "auto":
      bn_output = os.path.splitext(fn_json)[0]
      fn_output = bn_output + ".txt"
      print(f"Auto-created output text Chat file: {fn_output}")
   else:
      if not os.path.isfile(fn_output):
         print(f"Output Chat file will be created: {fn_output}")
      else:
         print(f"Output Chat file will be overwritten: {fn_output}")
else:
   print("No output Chat file specified with --output. Use --help argument to show help information.")
   exit(0)

if (args.print):
   show_console = True
else:
   show_console = False

if show_console:
   print("\nChat messages:")
   print("--------------------------------------------------------------------")

formated_json = list()
with open(fn_json, 'r', encoding='utf-8') as f_json:
   while r_line := f_json.readline():
      r_line = r_line.rstrip()
      l_json = json.loads(r_line)
      formated_json.append(l_json)

with open(fn_output, 'w', encoding='utf-8') as f_output:
   for element in formated_json:
      chat_msgs_items = element['replayChatItemAction']['actions'][0]["addChatItemAction"]['item']

      if 'liveChatViewerEngagementMessageRenderer' in chat_msgs_items:
         chat_msgs = chat_msgs_items['liveChatViewerEngagementMessageRenderer']
      elif 'liveChatTextMessageRenderer' in chat_msgs_items:
         chat_msgs = chat_msgs_items['liveChatTextMessageRenderer']
      else:
         continue

      if 'message' in chat_msgs:
         msgs = chat_msgs['message']['runs']
         t_msg = ""

         for msg in msgs:
            url = ""

            if 'navigationEndpoint' in msg:
               url = msg['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
               url_pos = url.find('&q=http')
               url = url[url_pos + 3:]         
               url=url.replace('%2F', '/')
               url=url.replace('%3F', '?')
               url=url.replace('%3D', '=')
               url=url.replace('%3A', ':')
               url=url.replace('%26', '&')

            if 'text' in msg:
               if url != "":
                  t_msg += url + " "
               else:
                  t_msg += msg['text']
         
         t_msg = t_msg[0:-1]
         
         if 'authorName' in chat_msgs:
            author = chat_msgs['authorName']['simpleText']
         else:
            author = "???"
         if 'timestampText' in chat_msgs:
            timestamp = chat_msgs['timestampText']['simpleText']
         else:
            timestamp = "???"

      if timestamp != "???" and author != "???" and t_msg != "":
         line_write = timestamp + " | " + author + ": " + t_msg   
         if show_console:
            print(line_write)               
         f_output.write(line_write + "\n")

if show_console:
   print("--------------------------------------------------------------------\n")

print(f"Converted JSON file {fn_json} to text file {fn_output}\n")
