# my_project
## complexity project
### task1:- add logger to the complexity project

project log file is <C:\Users\user\eclipse-workspace\complexity_project\logfiles\__20230426_170939__3697017c62772d71b4445895933026a4.log>
+******************************************************************************+

![fibonacci_timing_0_to_5](https://user-images.githubusercontent.com/130226497/234666965-78f1f452-f289-424b-9e60-225fa7fb96a7.png)

n,recursive,dynamic

0,1.6509999999581026e-05,1.5617999999939514e-05

1,2.6769999998954574e-06,2.677999999978198e-06

2,6.246999999959257e-06,6.694000000084799e-06

3,9.370999999980256e-06,7.139999999683511e-06

4,1.6063999999982315e-05,7.1400000001276e-06

## GCcalc project
### task2:-Add a logger method and calculate GC frequency for all miRNA in human, mouse and rat in the mature sequence.

#### project log file and GC average for human(hsa) miRNA in the mature.fa data
fasta file is <C:\Users\user\AP\day1\data\mature.fa>
speciesCode is <hsa>
project log file is
<C:\Users\user\eclipseworkspace\logger_GCcalc_project\logfiles\mature__20230426_214355__3697017c62772d71b4445895933026a4.log>
found <2656> sequences
average GC % = <70.05512368618675>
#### project log file and GC average for mouse(mmu) miRNA in the mature.fa data
fasta file is <C:\Users\user\AP\day1\data\mature.fa>
speciesCode is <mmu>
+******************************************************************************+
project log file is <C:\Users\user\eclipse-workspace\logger_GCcalc_project\logfiles\mature__20230426_214834__3697017c62772d71b4445895933026a4.log>
+******************************************************************************+
found <1978> sequences
average GC % = <70.50310821391368>
#### project log file and GC average for rat(rno) miRNA in the mature.fa data
fasta file is <C:\Users\user\AP\day1\data\mature.fa>
speciesCode is <rno>
+******************************************************************************+
project log file is <C:\Users\user\eclipse-workspace\logger_GCcalc_project\logfiles\mature__20230426_215135__3697017c62772d71b4445895933026a4.log>
+******************************************************************************+
found <764> sequences
average GC % = <67.4683526671524>
### task3:-Generate logo plots for all miRNAs in mouse, human and rat in mature data
#### unique seed region and logoplot for mouse(mmu) miRNA in mature data
load sequences from fasta file <C:\Users\user\AP\day1\data\mature.fa>
loaded <48885> sequences and kept <1978> with species code [mmu]
1978
seed region is defined to run from <2>--><8>
found <1588> unique seed sequences

          A         C         G         T
0  0.241814  0.243703  0.291562  0.222922
1  0.236146  0.211587  0.301008  0.251259
2  0.205919  0.250630  0.335013  0.208438
3  0.217884  0.220403  0.307305  0.254408
4  0.211587  0.241814  0.286524  0.260076
5  0.217254  0.246851  0.301008  0.234887
6  0.212217  0.270151  0.253778  0.263854

![mature__uniqseeds_logoplt](https://user-images.githubusercontent.com/130226497/234679104-c3de4d58-9ad0-4877-9868-215b1bad696e.png)

#### unique seed region and logoplot for human(hsa) miRNA in mature.fa data
load sequences from fasta file <C:\Users\user\AP\day1\data\mature.fa>
loaded <48885> sequences and kept <2656> with species code [hsa]
2656
seed region is defined to run from <2>--><8>
found <2094> unique seed sequences

          A         C         G         T
0  0.249284  0.236867  0.282235  0.231614
1  0.244986  0.227794  0.295129  0.232092
2  0.205826  0.247373  0.346705  0.200096
3  0.218243  0.225883  0.323782  0.232092
4  0.225883  0.257402  0.284623  0.232092
5  0.239733  0.244031  0.278415  0.237822
6  0.217287  0.267431  0.256447  0.258835

![mature__uniqseeds_logoplt](https://user-images.githubusercontent.com/130226497/234681040-53379728-24da-4458-8eab-c9c6a016c72d.png)

#### unique seed region and logoplot for rat(rno) miRNA in mature.fa data
load sequences from fasta file <C:\Users\user\AP\day1\data\mature.fa>
loaded <48885> sequences and kept <764> with species code [rno]
764
seed region is defined to run from <2>--><8>
found <635> unique seed sequences
write unique seed sequences to fasta file
output fasta file is <C:\Users\user\AP\day1\data\mature__uniqseeds.fa>

          A         C         G         T
0  0.277165  0.223622  0.288189  0.211024
1  0.251969  0.220472  0.270866  0.256693
2  0.242520  0.237795  0.307087  0.212598
3  0.244094  0.223622  0.264567  0.267717
4  0.226772  0.262992  0.231496  0.278740
5  0.277165  0.215748  0.255118  0.251969
6  0.222047  0.280315  0.222047  0.275591

![mature__uniqseeds_logoplt](https://user-images.githubusercontent.com/130226497/234683087-12f9f1c4-c5c2-4e00-bff6-6a1d3c6980a3.png)












