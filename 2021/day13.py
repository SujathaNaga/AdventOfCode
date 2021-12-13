#https://adventofcode.com/2021/day/1

import copy
from bisect import bisect_left
import re, os, sys
from itertools import chain
import math
from typing import DefaultDict, final
import time
from collections import Counter, defaultdict
from threading import Thread, Lock

input_main="""1101,291
221,448
1098,383
217,399
507,191
410,240
1036,449
208,241
469,548
1064,838
189,72
1198,812
107,483
900,206
902,325
430,7
801,834
1009,890
263,65
1255,379
328,502
537,703
724,763
126,521
788,127
544,484
110,36
243,28
1183,215
242,420
811,373
1228,325
567,880
798,250
5,264
165,362
140,126
915,596
835,806
1047,157
1123,222
72,654
1111,863
114,411
212,511
1071,603
1123,672
704,707
1191,558
944,137
1168,879
55,379
773,74
36,227
36,560
1048,856
209,151
1016,355
1012,428
528,616
902,390
489,532
350,528
790,18
666,759
224,191
761,560
571,602
329,698
330,806
1310,883
919,855
1250,119
1069,305
754,486
574,632
411,418
423,410
329,180
823,781
499,521
902,530
316,778
649,355
581,672
1101,603
1110,224
601,47
977,264
1297,340
743,294
463,343
652,134
73,446
5,508
946,891
698,609
1015,343
440,792
221,670
597,894
1153,763
798,187
946,521
1297,365
212,383
157,763
1228,894
939,494
1039,227
463,551
132,16
536,241
1071,561
1027,876
567,462
199,438
1009,789
271,299
1170,350
557,613
360,847
1309,84
58,474
1184,0
709,847
711,47
885,613
179,75
87,630
577,677
1098,511
1086,7
145,284
939,176
33,301
373,736
733,217
841,346
192,445
147,311
192,837
818,653
330,866
610,628
306,66
850,497
246,812
162,784
207,227
1084,131
738,424
728,318
900,318
851,217
1086,66
684,169
391,407
798,431
1121,341
189,588
441,845
736,184
999,582
1061,417
406,168
773,820
715,458
649,386
1215,529
773,191
960,528
1111,438
67,29
946,821
126,392
268,868
897,305
1196,35
1119,551
60,319
72,128
126,278
1305,264
1243,522
455,438
393,281
552,319
1280,838
733,677
30,61
800,819
412,756
246,504
507,759
776,114
73,224
1305,284
984,872
1233,604
835,75
692,334
254,240
1310,358
144,371
1066,123
1078,810
509,386
1245,710
107,819
114,483
678,308
873,847
1103,227
463,327
1168,250
889,147
830,402
522,127
107,115
0,883
805,620
559,60
1176,298
897,133
1059,758
0,252
985,322
30,838
1282,101
1102,241
1028,653
1175,327
957,378
42,733
1145,625
373,343
763,411
459,343
338,436
360,47
246,437
907,86
77,677
594,575
801,386
723,29
283,876
189,621
1110,866
408,156
475,88
251,758
738,31
643,315
301,4
739,154
728,206
1247,487
644,211
330,200
507,583
333,182
5,91
294,399
848,57
609,191
343,311
995,252
221,224
1208,663
406,138
1163,311
1230,88
393,165
5,162
1064,530
43,3
653,628
985,362
1183,255
974,267
290,331
1299,362
266,775
1064,122
1093,47
392,38
65,184
572,613
571,544
520,428
1067,866
470,19
783,886
363,86
311,70
320,527
1066,206
221,560
1233,677
1049,165
1042,868
1143,333
1158,268
472,96
1256,894
224,887
565,821
391,65
1081,505
925,334
131,665
1094,410
761,224
818,205
609,43
677,700
738,613
927,719
582,318
808,716
960,472
28,437
946,563
803,311
33,593
850,311
364,521
502,884
856,614
1310,232
661,284
212,35
924,868
502,626
107,523
445,79
808,570
803,703
877,334
181,22
980,28
1245,415
502,716
947,86
107,380
1039,595
743,880
271,595
745,73
559,529
1173,889
78,829
105,782
115,369
1118,389
917,707
364,378
813,131
405,229
321,264
492,653
11,362
633,700
408,738
510,371
537,815
1277,749
187,222
50,497
875,16
599,827
1086,255
1064,156
1064,604
902,569
454,280
639,70
1200,36
107,878
986,806
137,374
1102,149
739,292
830,626
191,439
221,446
455,863
1173,247
1069,589
624,838
1176,876
880,35
499,373
353,82
632,808
1206,68
541,397
321,179
30,232
879,122
241,305
1061,5
295,343
512,879
937,343
164,43
1305,539
610,266
551,548
454,28
661,386
994,340
1280,61
671,70
618,373
462,718
980,638
281,36
460,497
338,884
1295,824
393,729
879,772
502,268
1009,154
386,868
447,227
1138,542
296,609
1310,11
408,530
897,761
192,53
981,698
54,166
1064,390
147,415
587,29
1064,856
537,596
1173,647
1020,563
774,241
684,457
654,11
1111,86
798,879
559,813
1158,716
192,176
415,732
842,752
115,77
82,325
1097,621
966,598
423,92
1119,119
60,575
1071,499
539,817
395,596
1280,662
383,609
873,822
1215,813
162,241
857,840
763,859
1305,162
728,240
350,586
231,81
739,740
242,868
534,114
877,448
453,840
1215,386
1265,407
487,781
152,716
629,516
353,890
1256,0
1285,452
902,156
502,324
1228,613
706,588
115,817
576,513
1086,120
1129,834
919,289
629,442
950,47
686,838
1183,568
994,100
498,815
334,880
373,372
830,268
1071,268
137,520
869,845
599,515
599,47
577,604
348,828
902,290
430,828
440,515
1168,431
339,252
957,82
971,252
710,894
333,732
838,96
1272,332
102,127
1145,849
1019,826
217,495
119,558
1268,733
1039,609
377,551
701,43
982,683
325,572
1260,812
1274,112
290,597
1068,138
547,563
1237,672
343,70
137,140
50,588
454,614
118,205
498,367
353,378
835,88
114,859
1158,772
1145,362
1183,639
169,67
711,67
1226,868
1268,833
301,789
677,642
995,763
582,576
316,554
904,138
339,642
1304,527
22,422
1129,872
460,728
454,168
1196,411
763,331
58,292
1227,350
65,483
848,841
729,0
634,427
1195,77
1149,84
140,544
933,551
200,728
985,124
656,11
545,616
459,677
957,341
1103,652
1119,455
107,688
104,826
1101,74
325,124
1227,740
502,10
1203,523
527,7
1158,570
290,821
1207,346
1242,763
1064,56
194,728
431,122
1068,868
435,16
611,242
462,53
115,525
161,84
462,885
541,497
788,654
1123,224
1120,567
249,5
771,817
1154,544
405,889
561,572
994,794
396,91
729,672
869,273
542,306
644,759
1247,381
1020,73
1165,508
1094,415
736,595
801,60
907,534
1308,246
872,31
207,652
1118,837
30,609
887,92
595,458
895,732
1064,38
82,613
1128,544
325,362
85,122
1146,43
454,224
517,199
433,446
1212,408
1163,583
5,732
589,710
364,891
1203,75
1033,679
480,626
865,255
246,200
316,359
1052,131
438,484
15,70
982,470
609,851
609,372
194,807
900,688
981,124
957,553
1247,183
507,31
1233,290
1232,392
1089,560
982,502
134,428
600,0
1193,752
459,665
1020,740
316,100
328,22
1305,508
126,894
895,716
328,424
550,516
880,66
1265,191
1274,821
446,653
393,184
902,604
787,665
856,280
1068,26
1310,502
1056,206
1174,786
1091,155
855,438
348,380
927,623
759,548
972,458
191,775
792,786
648,73
851,677
604,588
1280,659
986,190
1119,775
455,326
187,224
1086,319
165,700
612,61
705,215
582,654
581,224
1196,483
364,331
441,49
831,26
902,255
488,306
869,621
371,204
878,516
107,75
768,515
835,523
989,264
117,703
971,28
221,672
678,586
745,821
599,399
1274,597
273,47
145,386
1066,0
1200,31
135,327
986,88
328,683
589,483
1260,497
59,458
1195,525
1304,821
1091,739
957,452
358,733
1170,544
1110,222
856,149
1168,655
788,543
664,715
1089,448
118,653
960,250
22,472
485,60
373,522
888,532
244,894
576,138
728,576
147,479
324,88
28,101
681,292
612,833
209,291
387,346
898,756
1279,439
967,824
371,718
1111,120
893,73
1089,224
698,61
261,710
316,116
1168,239
315,642
1225,122
1195,817
246,738
224,639
1121,247
581,222
1223,630
338,564
152,10
271,609
594,270
242,474
350,250
194,280
261,165
222,378
493,717
410,771
743,462
739,544
423,372
358,609
1278,623
662,73
1252,602
224,774
469,346
213,621
224,319
454,390
1039,299
263,39
1274,521
570,302
788,351
177,274
229,389
36,521
773,703
763,819
527,886
986,28
656,883
137,72
855,86
711,515
1203,483
423,81
946,292
541,845
1019,516
329,250
142,879
1111,422
1158,535
463,439
165,208
848,885
480,402
25,442
432,516
145,162
221,334
25,292
95,365
98,408
1193,372
565,73

fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6"""

input1="""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

class my_logger:
    def __init__(self) -> None:
        self._logfile=open('./2021/'+os.path.basename(sys.argv[0])+'.log.txt','w+')
        self._logfilemutex=Lock()
        self._enable=True

    def write(self, line):
        if not self._enable:
            return 

        self._logfilemutex.acquire()
        try:
            self._logfile.write(line+'\n')
        finally:
            self._logfilemutex.release()
    
    def __del__(self) -> None:
        self._logfile.close()
    
    def enable(self, e):
        self._enable=e

global_logger=my_logger()
# global_logger.enable(False)
# global_logger.write(' '.join(['\n\t', thread_name, 'branch-end-len', str(len(main_list)), str(main_list)]))

class ThreadSafeData:
    def __init__(self, data) -> None:
        self._data=data
        self._mutex=Lock()
    
    def append(self, d):
        self._mutex.acquire()
        try:
            self._data+=d
        finally:
            self._mutex.release()

    def add(self, d):
        self._mutex.acquire()
        try:
            self._data+=d
        finally:
            self._mutex.release()
        
    def get_copy(self):
        return_data=None
        self._mutex.acquire()
        try:
            return_data=copy.deepcopy(self._data)
        finally:
            self._mutex.release()
        
        return return_data
        

class WinException(BaseException):
    pass

class ErrorException(BaseException):
    pass

class point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

class line:
    def __init__(self,coordinates) -> None:
        self.point1 = point(coordinates[0], coordinates[1])
        self.point2 = point(coordinates[2], coordinates[3])

    def get_line_points_hor_vert(self):
        # Bresenham algorithm
        number_of_points=max(abs(self.point1.x - self.point2.x), abs(self.point1.y-self.point2.y))
        number_of_points-=1 # adjust for end points
        x_spacing=(self.point2.x-self.point1.x)/(number_of_points+1)
        y_spacing=(self.point2.y-self.point1.y)/(number_of_points+1)
        return [self.point1] + [point(self.point1.x + i * x_spacing, self.point1.y + i * y_spacing) for i in range(1, number_of_points+1)] + [self.point2]


class MyThread:
    def __init__(self, t, mut) -> None:
        self._thread=t
        self._mutex=mut

def get_key(dict1, value):
    for k,v in dict1.items():
        if v==value:
            return k
    return None

def get_keys_from_len_of_key(dict1, length):
    keys=[]
    for k,v in dict1.items():
        if len(k)==length:
            keys.append(k)
    return keys

def get_keys_from_len_of_value(dict1, length):
    keys=[]
    for k,v in dict1.items():
        if len(v)==length:
            keys.append(k)
    return keys

def get_keys_from_value(dict1, value):
    keys=[]
    for k,v in dict1.items():
        if v==value:
            keys.append(k)
    return keys

def has_all_chars(input_string, string2):
    for s in string2:
        if s not in input_string:
            return False
    return True

def get_all_indices_of_element(list1,element):
    final_list=[]
    for i in range(len(list1)):
        if list1[i]==element:
            final_list.append(i)
    return final_list

#####################################################################################

lines = input1.split('\n')
lines = input_main.split('\n')

folds=[]
map_data=defaultdict(lambda:[])

def funca():
    global folds
    global map_data

    for fold in folds:
        if fold[0]=='y':
            # horizontal fold up
            sorted_keys=sorted(map_data.keys())
            fold_x_index = bisect_left(sorted_keys, fold[1])
            for index in range(fold_x_index, len(sorted_keys)):
                current_x=sorted_keys[index]
                # fold up
                new_x=fold[1] - abs((current_x-fold[1]))
                # merge. remove duplicates
                map_data[new_x]=sorted(list(set(map_data[new_x]+map_data[current_x])))
            
            [map_data.pop(sorted_keys[i]) for i in range(fold_x_index, len(sorted_keys))]
        elif fold[0]=='x':
            # vertical fold left. 
            sorted_keys=sorted(map_data.keys())
            for k in sorted_keys:
                sorted_list=map_data[k]
                fold_y_index=bisect_left(sorted_list, fold[1])
                new_ys=[]
                for index in range(fold_y_index, len(sorted_list)):
                    # fold left
                    new_y=fold[1]-(sorted_list[index]-fold[1])
                    # merge. do not add duplicates
                    if new_y not in sorted_list:
                        new_ys.append(new_y)

                del sorted_list[fold_y_index:]
                sorted_list.extend(new_ys)
                sorted_list.sort()

        print('a',fold, sum([len(v) for v in map_data.values()]))

    max_col=max(max(v_list) for v_list in map_data.values())
    sorted_keys=sorted(map_data.keys())
    output = ""
    for key in sorted_keys:
        for i in range(max_col+1):
            output+='#' if i in map_data[key] else ' '
        output+="\n"
    print(output)
    # RPCKFBLR

for line in lines:
    if 'fold along ' in line:
        v=line.split(' ')[-1]
        axis,v=v.split('=')
        folds.append((axis,int(v)))
    elif line != '':
        y,x=line.split(',')
        map_data[int(x)].append(int(y))

for m in map_data:
    map_data[m].sort()

try:
    start=time.time()
    funca()
    print('time',time.time()-start)

except WinException as e:
    pass

# 424 too low

start=time.time()
# funcb(lines)
print('time',time.time()-start)
