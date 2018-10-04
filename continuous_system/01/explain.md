# MPIを用いた merge sort の並列化

## 参考ページ

- [MPIの仕様](http://www.cv.titech.ac.jp/~hiro-lab/study/mpi_reference/)

## 自分が試した時の結果

- Nは入力データのサイズ
- pは使用するプロセス数(mergeを簡単にするため、pは2の累乗の値にしています)

| N = (128000 * i) | 実行時間 |
----|----
| 1 | 0.038021 |
| 2 | 0.039414 |
| 3 | 0.041198 |
| 4 | 0.044974 |
| 5 | 0.047959 |
| 10 | 0.055121 |
| 20 | 0.074026 |
| 30 | 0.092743 |
| 40 | 0.111292 |
| 50 | 0.133221 |
| 60 | 0.152855 |
| 70 | 0.171901 |
| 80 | 0.195506 |
| 85 | 0.202474 |
| 90 | 0.216483 |

- 並列化による計算量は、

<img src = "https://latex.codecogs.com/gif.latex?O(N&space;&plus;&space;\frac{N}{p}\log&space;{\frac{N}{p}})" />

のようになります。これは、nlognで増えていく計算量で、係数が小さくなります。下のグラフを見ると、実験結果とよく合致しますね(諸説)

- 上の表をグラフにしたものは[figure.png](https://github.com/BOBO1997/IS_3A/blob/master/continuous_system/01/figure.png)にあります。
