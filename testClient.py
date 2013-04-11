from serviceClient import serviceClient 

client=serviceClient("https://v1.eligibleapi.net/service/list.json","TEST")
responce=client.get_responce("1","Group Health Plan - CMR GROUP HEALTH PLAN (GHP)","184","Thomason","Mark","1928384219","W120923801","Austen","Jane","1955-12-14")
responce.print_data()

