## Examples  
Below is the .txt-formatted output of meta-analyses conducted using the {meta} package in R and the table which is generated using a Textab script.

### R output
```
Details on meta-analytical method:
- Inverse variance method
- Restricted maximum-likelihood estimator for tau^2
- Q-Profile method for confidence interval of tau^2 and tau
- Hartung-Knapp adjustment for random effects model (df = 10)
- Hedges' g (bias corrected standardised mean difference; using exact formulae)
Review:     SFI

                         SMD             95%-CI %W(random)
Yu (2020)             0.9032 [ 0.1713;  1.6350]       18.2
Yu (2022)            -1.1587 [-1.9146; -0.4028]       18.1
Garcia Garcia (2023) -0.3793 [-1.5256;  0.7669]       15.5
Garcia Garcia (2023)  0.8306 [-0.3697;  2.0308]       15.2
Philips (2018)       -0.4306 [-1.5810;  0.7199]       15.5
Sondell (Yu 2020)    -1.8622 [-2.7083; -1.0161]       17.5

Number of studies: k = 6
Number of observations: o = 132 (o.e = 66, o.c = 66)

                         SMD            95%-CI     t p-value
Random effects model -0.3709 [-1.5303; 0.7885] -0.82  0.4483

Quantifying heterogeneity:
 tau^2 = 1.0188 [0.2601; 6.8993]; tau = 1.0094 [0.5100; 2.6267]
 I^2 = 84.2% [67.1%; 92.4%]; H = 2.51 [1.74; 3.62]

Test of heterogeneity:
     Q d.f.  p-value
 31.56    5 < 0.0001

Details on meta-analytical method:
- Inverse variance method
- Restricted maximum-likelihood estimator for tau^2
- Q-Profile method for confidence interval of tau^2 and tau
- Hartung-Knapp adjustment for random effects model (df = 5)
- Hedges' g (bias corrected standardised mean difference; using exact formulae)
Review:     Myelin Thickness

                         SMD              95%-CI %W(random)
Wang (2015)          -0.4023 [ -1.6617;  0.8571]        9.0
Boriani (2017)        0.3096 [ -0.9417;  1.5610]        9.1
Qiu (2020)           -6.4080 [-10.1622; -2.6537]        4.3
Takeuchi (2021)      -1.4163 [ -2.8826;  0.0500]        8.6
Yu (2022)            -1.9468 [ -2.8058; -1.0879]        9.8
Garcia Garcia (2023) -2.2418 [ -3.8062; -0.6774]        8.4
Garcia Garcia (2023) -2.4618 [ -4.1011; -0.8224]        8.3
Kim (2016)            0.1642 [ -0.8179;  1.1464]        9.6
Vasudevan (2014)     -1.8097 [ -3.2382; -0.3811]        8.7
Wakimura (2014)      -0.2968 [ -1.5472;  0.9536]        9.1
Cai (2017)           -2.1399 [ -3.6707; -0.6090]        8.5
Ji (2020)            -6.4456 [ -8.8279; -4.0633]        6.7

Number of studies: k = 12
Number of observations: o = 166 (o.e = 83, o.c = 83)

                         SMD             95%-CI     t p-value
Random effects model -1.7709 [-3.0285; -0.5133] -3.10  0.0101

Quantifying heterogeneity:
 tau^2 = 2.5831 [1.0792; 12.7006]; tau = 1.6072 [1.0389; 3.5638]
 I^2 = 78.6% [63.2%; 87.6%]; H = 2.16 [1.65; 2.84]

Test of heterogeneity:
     Q d.f.  p-value
 51.51   11 < 0.0001

Details on meta-analytical method:
- Inverse variance method
- Restricted maximum-likelihood estimator for tau^2
- Q-Profile method for confidence interval of tau^2 and tau
- Hartung-Knapp adjustment for random effects model (df = 11)
- Hedges' g (bias corrected standardised mean difference; using exact formulae)
```
### Textab output

| Title | Number of Studies | Pooled Effect Size (95% CI) | P-value | I2 |
| :---- | :---------------- | :-------------------------- | :------ | :- |
| TA Muscle | 13 | -1.7421 (-2.4713 - -1.0129) | 0.0002 | 60.0% |
| GC Muscle | 12 | -1.8486 (-2.5641 - -1.1331) | 0.0001 | 49.8% |
| CMAP | 15 | -2.9389 (-4.3794 - -1.4985) | 0.0006 | 84.2% |
| NCV | 11 | -3.2516 (-5.5083 - -0.9948) | 0.0093 | 84.4% | 
| SFI | 6 | -0.3709 (-1.5303 - 0.7885) | 0.4483 | 84.2% | 
| Myelin Thickness | 12 | -1.7709 (-3.0285 - -0.5133) | 0.0101 | 78.6% |
