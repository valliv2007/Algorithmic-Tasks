"""Let's define increasing numbers as the numbers whose digits, read from left to right, are never less than 
the previous ones: 234559 is an example of increasing number.

Conversely, decreasing numbers have all the digits read from left to right so that no digits is bigger than 
the previous one: 97732 is an example of decreasing number.

You do not need to be the next Gauss to figure that all numbers with 1 or 2 digits are either increasing or 
decreasing: 00, 01, 02, ..., 98, 99 are all belonging to one of this categories (if not both, like 22 or 55): 
101 is indeed the first number which does NOT fall into either of the categories. 
Same goes for all the numbers up to 109, while 110 is again a decreasing number.

Now your task is rather easy to declare (a bit less to perform): you have to build a function to return the 
total occurrences of all the increasing or decreasing numbers below 10 raised to the xth power (x will always be >= 0).

To give you a starting point, there are a grand total of increasing and decreasing numbers as shown in the table:

Total	Below
1	     1
10	     10
100	     100
475	     1000
1675	10000
4954	100000
12952	1000000
This means that your function will have to behave like this:

total_inc_dec(0)==1
total_inc_dec(1)==10
total_inc_dec(2)==100
total_inc_dec(3)==475
total_inc_dec(4)==1675
total_inc_dec(5)==4954
total_inc_dec(6)==12952
Tips: efficiency and trying to figure out how it works are essential: with a brute force approach, 
some tests with larger numbers may take more than the total computing power currently on Earth to be finished 
n the short allotted time.

To make it even clearer, the increasing or decreasing numbers between in the range 101-200 are: 
[110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 122, 123, 124, 125, 126, 127, 128, 129, 133, 134, 135, 136, 137, 138, 139, 
144, 145, 146, 147, 148, 149, 155, 156, 157, 158, 159, 166, 167, 168, 169, 177, 178, 179, 188, 189, 199, 200], 
that is 47 of them. In the following range, 201-300, there are 41 of them and so on, getting rarer and rarer.

Trivia: just for the sake of your own curiosity, a number which is neither decreasing of increasing is called 
a bouncy number, like, say, 3848 or 37294; also, usually 0 is not considered being increasing, decreasing or bouncy, 
but it will be for the purpose of this kata"""


def total_inc_dec(x):
    ten = 10 ** x
    century = 100
    if x == 0:
        return 1
    elif x == 1:
        return 10
    elif x == 2:
        return 100
    count = century + 1
    i = 110
    num = 0
    while i < ten:
        num += 1
        direction = None
        # print(i)
        step = 0
        for j in range(1, len(str(i))):
            if (direction == 'more' and str(i)[j] < str(i)[j - 1]) or (direction == 'less' and str(i)[j] > str(i)[j - 1]):
                if str(i)[j] < str(i)[j - 1]:
                    step = (int(str(i)[j - 1]) - int(str(i)[j])) * 10**(len(str(i)) - 1 -j)
                if str(i)[j] > str(i)[j - 1]:
                    step = (10 - int(str(i)[j])) * 10**(len(str(i)) - 1 -j)
                break
            else:
                if str(i)[j] < str(i)[j - 1]:
                    direction = 'less'
                elif str(i)[j] > str(i)[j - 1]:
                    direction = 'more'
                if j == len(str(i)) - 1:
                    if str(i)[j] < str(i)[j - 1]:
                        step +=  int(str(i)[j - 1]) - int(str(i)[j])
                    elif str(i)[j] > str(i)[j - 1]:
                        step = 10 - int(str(i)[j])
                    else:
                        step = 1
                    count += step
        i += step
    print(num)
    return count


print(total_inc_dec(9))
100
111
112
113
114
115
116
117
118
119
122
123
124
125
126
127
128
129
133
134
135
136
137
138
139
140
144
145
146
147
148
149
155
156
157
158
159
166
167
168
169
177
178
179
188
189
199
200
210
211
220
221
222
223
224
225
226
227
228
229
233
234
235
236
237
238
239
244
245
246
247
248
249
255
256
257
258
259
266
267
268
269
277
278
279
288
289
299
300
310
311
320
321
322
330
331
332
333
334
335
336
337
338
339
344
345
346
347
348
349
355
356
357
358
359
366
367
368
369
377
378
379
388
389
399
400
410
411
420
421
422
430
431
432
433
440
441
442
443
444
445
446
447
448
449
455
456
457
458
459
466
467
468
469
477
478
479
488
489
499
500
510
511
520
521
522
530
531
532
533
540
541
542
543
544
550
551
552
553
554
555
556
557
558
559
566
567
568
569
577
578
579
588
589
599
600
610
611
620
621
622
630
631
632
633
640
641
642
643
644
650
651
652
653
654
655
660
661
662
663
664
665
666
667
668
669
677
678
679
688
689
699
700
710
711
720
721
722
730
731
732
733
740
741
742
743
744
750
751
752
753
754
755
760
761
762
763
764
765
766
770
771
772
773
774
775
776
777
778
779
788
789
799