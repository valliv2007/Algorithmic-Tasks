a = '424 752 845 586 173 505 432 537 608 732 698 655 248 690 477 777 344 3 928 744 450 275 519 302 627 823 314 956 708 586 664 155 456 189 327 723 111 694 498 391 181 706 302 867 311 541 293 812 425 817 153 466 413 1000 264 471 930 565 545 955 875 181 895 861 805 448 983 1000 522 481 878 841 28 922 484 211 390 475 621 723 76 517 771 229 2 681 898 122 770 659 642 672 201 952 322 755 24 689 83 93'
b = [int(i) for i in a.split()]
b.sort()
print(b)