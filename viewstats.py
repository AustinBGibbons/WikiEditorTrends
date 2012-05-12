views= {'20076': 1304272, '20077': 1316164, '20074': 1362904, '20075': 1526718, '20072': 1420974, '20073': 1593049, '20071': 1654658, '20078': 1287675, '20079': 1152009, '200211': 2442361, '200210': 3311413, '200212': 2478122, '20092': 784920, '20043': 4330477, '20042': 3165034, '20041': 2579048, '20047': 3041639, '20046': 2926007, '20045': 3453522, '20044': 4581372, '20049': 2927424, '20048': 3344864, '200812': 894765, '200811': 764423, '200810': 817640, '20111': 651112, '20112': 117809, '20058': 3193466, '20059': 2526273, '20054': 2889278, '20055': 2640926, '20056': 2911173, '20057': 3647973, '20051': 2276730, '20052': 1915030, '20053': 2501167, '200412': 2898411, '200411': 2836191, '200410': 2894915, '200710': 1010644, '200711': 1004592, '200712': 1009403, '20108': 665104, '20109': 662718, '20106': 749232, '20107': 669194, '20104': 662710, '20105': 685285, '20102': 571428, '20103': 666305, '20101': 685239, '20029': 3278360, '20028': 2905068, '20021': 1617681, '20023': 2423490, '20022': 5131227, '20025': 1504376, '20024': 1488683, '20027': 2012856, '20026': 2001003, '20038': 2723869, '20039': 2335809, '20032': 2046895, '20033': 1853720, '20031': 3308530, '20036': 2306691, '20037': 2480195, '20034': 2370215, '20035': 2409198, '201010': 714290, '201011': 628290, '201012': 618733, '200310': 1884531, '200311': 2495502, '200312': 2531231, '20093': 883146, '20089': 734147, '20088': 862774, '20087': 922711, '20086': 980947, '20085': 878436, '20084': 912821, '20083': 1053112, '20082': 1157121, '20081': 1050403, '20012': 193487, '200911': 657990, '20098': 754927, '20099': 688902, '200112': 2289745, '20091': 808290, '200110': 8050084, '200111': 6019119, '20094': 762784, '20095': 851928, '20096': 696862, '20097': 763329, '200912': 766848, '20011': 34551, '200910': 718884, '20013': 843064, '20014': 594122, '20015': 1654953, '20016': 629891, '20017': 1338047, '20018': 2153437, '20019': 4424265, '200512': 2611777, '200510': 2724632, '200511': 2363274, '200611': 1503699, '200610': 1698525, '200612': 1601778, '20065': 2081734, '20064': 2202715, '20067': 2300079, '20066': 2231791, '20061': 2449873, '20063': 2314990, '20062': 2069753, '20069': 1752044, '20068': 2177687}

years = {}
for year in views : 
	if year[:4] not in years : years[year[:4]] = 0
	years[year[:4]] += views[year]

keys = years.keys()
keys.sort()
for year in keys:
	print year, years[year]

