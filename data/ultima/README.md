---
license: other
license_name: umamusume-derivativework-guidelines
license_link: https://umamusume.jp/derivativework_guidelines/
task_categories:
- object-detection
language:
- en
pretty_name: ultima_yolo
size_categories:
- 1K<n<10K
---


# About ULTIMA-YOLO

This is a repository for subproject of [ULTIMA](https://huggingface.co/datasets/UmaDiffusion/ULTIMA).

ULTIMA-YOLO contains yolo-format bounding box of Uma Musume and corresponding image pair.


```text
label_data.txt
[object_id] [x_center] [y_center] [width] [height]
[object_id] [x_center] [y_center] [width] [height]
...
```

132 characters in Uma Musume are in ULTIMA-YOLO dataset.

Trained Model, based on [yolov9-e](https://github.com/WongKinYiu/yolov9), is in [ULTIMA-YOLOv9](https://huggingface.co/UmaDiffusion/ULTIMA-YOLOv9)


# Statistics
- Train: 3,991 images
- Val: 399 images
- All labels have been manually created through human effort, with workers ethically compensated with "passion pay", a term came from south korea.
- Each image is named to indicate its source.


| Character Name | # in Train | # in Val | Precision | Recall | mAP50 | mAP50-95 |
|:------------------:|:---:|:---:|:---:|:---:|:---:|:---:|
| Agnes Tachyon      | 187 |  35 | 0.957 | 0.886 | 0.961 | 0.765 |
| Air Groove         |  87 |  12 | 1 | 0.835 | 0.933 | 0.713 |
| Air Shakur         |  75 |  12 | 0.986 | 1 | 0.995 | 0.909 |
| Akikawa Yayoi      |  25 |   3 | 1 | 0.693 | 0.995 | 0.648 |
| Admire Vega        |  74 |  16 | 1 | 0.754 | 0.894 | 0.707 |
| Agnes Digital      |  50 |   6 | 0.992 | 0.833 | 0.972 | 0.803 |
| Anshinzawa Sasami  |  25 |   1 | 0.956 | 1 | 0.995 | 0.796 |
| Aston Machan       |  55 |   3 | 1 | 0.726 | 0.995 | 0.912 |
| Bamboo Memory      |  41 |   3 | 0.97 | 1 | 0.995 | 0.895 |
| Biko Pegasus       |  34 |   3 | 0.972 | 1 | 0.995 | 0.84 |
| Byerley Turk       |  43 |   2 | 0.951 | 1 | 0.995 | 0.855 |
| Bitter Glace       |  24 |   0 | 0.888 | 0.875 | 0.944 | 0.776 |
| Biwa Hayahide      |  52 |   8 | 0.821 | 1 | 0.995 | 0.846 |
| Copano Rickey      |  51 |   5 | 0.969 | 0.667 | 0.864 | 0.69 |
| Curren Chan        |  54 |   9 | 0.996 | 1 | 0.995 | 0.801 |
| Cheval Grand       |  43 |  13 | 0.998 | 1 | 0.995 | 0.783 |
| Twin Turbo         | 120 |  13 | 0.982 | 1 | 0.995 | 0.842 |
| Daiichi Ruby       |  57 |   5 | 0.963 | 1 | 0.995 | 0.949 |
| Darley Arabian     |  48 |   2 | 1 | 0.837 | 0.995 | 0.819 |
| Daring Tact        |  62 |   5 | 0.997 | 1 | 0.995 | 0.841 |
| Daitaku Helios     | 100 |  11 | 1 | 0.903 | 0.961 | 0.787 |
| Daiwa Scarlet      | 114 |  19 | 0.987 | 1 | 0.995 | 0.707 |
| El Condor Pasa     |  65 |   6 | 0.951 | 1 | 0.995 | 0.808 |
| Eishin Flash       |  39 |   5 | 0.853 | 1 | 0.995 | 0.927 |
| Fuji Kiseki        |  48 |   6 | 1 | 0.875 | 0.995 | 0.88 |
| Fine Motion        |  55 |   7 | 0.989 | 0.875 | 0.906 | 0.71 |
| Gold City          |  49 |   8 | 0.942 | 0.938 | 0.991 | 0.81 |
| Gold Ship          | 146 |  16 | 0.858 | 1 | 0.995 | 0.895 |
| Godolphin Barb     |  44 |   2 | 0.84 | 0.833 | 0.851 | 0.659 |
| Grass Wonder       |  74 |   6 | 1 | 0.797 | 0.995 | 0.792 |
| Hishi Akebono      |  39 |   4 | 0.989 | 1 | 0.995 | 0.766 |
| Hishi Amazon       |  46 |   6 | 0.993 | 1 | 0.995 | 0.835 |
| Hayakawa Tazuna    |  34 |   5 | 1 | 0.659 | 0.922 | 0.638 |
| Hishi Miracle      |  52 |   6 | 0.971 | 0.75 | 0.945 | 0.769 |
| Happy Meek         |  51 |   4 | 1 | 0.787 | 0.938 | 0.808 |
| Hokko Tarumae      |  50 |   9 | 1 | 0.678 | 0.995 | 0.76 |
| Haru Urara         |  69 |   9 | 0.986 | 0.917 | 0.989 | 0.747 |
| Ikuno Dictus       |  96 |  12 | 0.873 | 1 | 0.995 | 0.858 |
| Ines Fujin         |  41 |   7 | 0.947 | 1 | 0.995 | 0.898 |
| Inari One          |  46 |   2 | 0.856 | 1 | 0.995 | 0.656 |
| Jungle Pocket      |  53 |   6 | 1 | 0.85 | 0.995 | 0.747 |
| King Halo          |  77 |   6 | 0.975 | 1 | 0.995 | 0.773 |
| Kashimoto Riko     |  34 |   3 | 1 | 0.778 | 0.995 | 0.823 |
| Kiryuin Aoi        |  44 |   4 | 0.997 | 0.895 | 0.929 | 0.712 |
| Kitasan Black      | 116 |  19 | 0.974 | 1 | 0.995 | 0.909 |
| K.S.Miracle        |  48 |   3 | 0.982 | 1 | 0.995 | 0.852 |
| Katsuragi Ace      |  43 |   4 | 0.989 | 1 | 0.995 | 0.881 |
| Kawakami Princess  |  50 |   7 | 0.975 | 1 | 0.995 | 0.841 |
| Little Cocon       |  51 |   3 | 1 | 0.567 | 0.995 | 0.796 |
| Light Hello        |  25 |   2 | 0.993 | 1 | 0.995 | 0.788 |
| Mr. C.B.           |  91 |  13 | 1 | 0.659 | 0.995 | 0.703 |
| Meisho Doto        |  59 |   7 | 0.988 | 1 | 0.995 | 0.782 |
| Mihono Bourbon     |  84 |  13 | 1 | 0.955 | 0.994 | 0.779 |
| Manhattan Cafe     | 144 |  32 | 0.876 | 0.884 | 0.967 | 0.797 |
| Mejiro Ardan       |  58 |   8 | 0.985 | 0.833 | 0.869 | 0.723 |
| Mejiro Bright      |  55 |   6 | 0.987 | 1 | 0.995 | 0.813 |
| Mejiro Dober       |  56 |   5 | 0.981 | 0.933 | 0.972 | 0.785 |
| Mejiro McQueen     | 272 |  30 | 0.98 | 1 | 0.995 | 0.873 |
| Mejiro Ryan        |  43 |   7 | 0.998 | 1 | 0.995 | 0.849 |
| Matikanefukukitaru |  52 |   7 | 1 | 0.952 | 0.995 | 0.719 |
| Matikanetannhauser |  87 |  13 | 0.996 | 1 | 0.995 | 0.81 |
| Mejiro Palmer      |  95 |  11 | 0.893 | 1 | 0.929 | 0.822 |
| Mejiro Ramonu      |  52 |   9 | 0.993 | 1 | 0.995 | 0.748 |
| Maruzensky         |  43 |   7 | 0.984 | 1 | 0.995 | 0.684 |
| Marvelous Sunday   |  40 |   6 | 1 | 0.702 | 0.995 | 0.668 |
| Nakayama Festa     |  47 |   7 | 0.992 | 1 | 0.995 | 0.829 |
| Nice Nature        |  96 |   8 | 0.993 | 1 | 0.995 | 0.723 |
| Narita Brian       |  86 |  13 | 0.827 | 1 | 0.962 | 0.778 |
| Narita Taishin     |  55 |   5 | 0.899 | 0.857 | 0.978 | 0.938 |
| Nishino Flower     |  48 |   7 | 0.97 | 1 | 0.995 | 0.72 |
| Narita Top Road    |  50 |   9 | 0.988 | 1 | 0.995 | 0.834 |
| Oguri Cap          |  94 |  10 | 0.997 | 0.92 | 0.945 | 0.744 |
| Rice Shower        | 165 |  25 | 0.992 | 1 | 0.995 | 0.89 |
| Sakura Bakushin O  |  55 |   7 | 1 | 0.949 | 0.995 | 0.795 |
| Symboli Rudolf     | 157 |  17 | 0.987 | 0.889 | 0.975 | 0.748 |
| Sakura Chiyono O   |  48 |   9 | 0.946 | 0.8 | 0.941 | 0.835 |
| Seiun Sky          |  72 |  10 | 0.98 | 1 | 0.995 | 0.842 |
| Sakura Laurel      |  44 |   6 | 0.944 | 1 | 0.995 | 0.895 |
| Shinko Windy       |  46 |   1 | 0.96 | 1 | 0.995 | 0.949 |
| Seeking the Pearl  |  34 |   2 | 0.985 | 1 | 0.995 | 0.844 |
| Symboli Kris S     |  68 |   6 | 0.87 | 0.958 | 0.943 | 0.728 |
| Smart Falcon       |  53 |   7 | 0.976 | 1 | 0.995 | 0.876 |
| Super Creek        |  48 |   4 | 1 | 0.959 | 0.995 | 0.736 |
| Special Week       | 147 |  14 | 1 | 0.975 | 0.995 | 0.777 |
| Silence Suzuka     | 129 |  18 | 0.993 | 1 | 0.995 | 0.84 |
| Sirius Symboli     |  60 |   9 | 0.962 | 1 | 0.995 | 0.849 |
| Satono Crown       |  47 |   2 | 0.993 | 0.75 | 0.925 | 0.746 |
| Satono Diamond     |  79 |  12 | 0.98 | 0.75 | 0.775 | 0.649 |
| Sweep Tosho        |  42 |   4 | 0.951 | 1 | 0.995 | 0.895 |
| Tap Dance City     |  49 |   4 | 0.995 | 1 | 0.995 | 0.832 |
| Taiki Shuttle      |  50 |   7 | 0.883 | 1 | 0.939 | 0.756 |
| Tokai Teio         | 239 |  23 | 0.994 | 1 | 0.995 | 0.56 |
| Tamamo Cross       |  59 |   6 | 1 | 0.86 | 0.99 | 0.748 |
| T.M. Opera O       |  85 |  13 | 0.986 | 1 | 0.995 | 0.838 |
| Tanino Gimlet      |  52 |   6 | 0.986 | 1 | 0.995 | 0.771 |
| Mayano Top Gun     |  70 |   5 | 1 | 0.824 | 0.995 | 0.787 |
| Tosen Jordan       |  68 |   9 | 0.959 | 1 | 0.995 | 0.801 |
| Tsurumaru Tsuyoshi |  38 |   2 | 0.984 | 1 | 0.995 | 0.736 |
| Neo Universe       |  47 |   5 | 1 | 0.806 | 0.945 | 0.753 |
| Vodka              | 110 |  15 | 0.954 | 1 | 0.995 | 0.895 |
| Wonder Acute       |  53 |   1 | 0.976 | 0.8 | 0.962 | 0.877 |
| Winning Ticket     |  47 |   5 | 0.997 | 1 | 0.995 | 0.889 |
| Yukino Bijin       |  44 |   7 | 1 | 0.965 | 0.995 | 0.904 |
| Yaeno Muteki       |  39 |   5 | 0.975 | 1 | 0.995 | 0.932 |
| Yamanin Zephyr     |  42 |   3 | 0.976 | 0.714 | 0.96 | 0.747 |
| Zenno Rob Roy      |  51 |   7 | 0.958 | 1 | 0.995 | 0.895 |
| Furioso            |  15 |   0 | 0.938 | 1 | 0.995 | 0.995 |
| Transcend          |  40 |   2 | 0.964 | 1 | 0.995 | 0.796 |
| Espoir City        |  30 |   1 | 0.939 | 1 | 0.995 | 0.895 |
| North Flight       |  40 |   2 | 0.946 | 1 | 0.995 | 0.597 |
| Dantsu Flame       |  30 |   1 | 0.878 | 1 | 0.995 | 0.895 |
| No Reason          |  26 |   0 | 0.961 | 0.667 | 0.699 | 0.53 |
| Still in Love      |  28 |   1 | 0.961 | 1 | 0.995 | 0.895 |
| Samson Big         |  25 |   1 | 0.891 | 1 | 0.995 | 0.697 |
| Sounds of Earth    |  53 |   3 | 0.972 | 1 | 0.995 | 0.857 |
| Royce and Royce    |  30 |   2 | 0.942 | 1 | 0.995 | 0.398 |
| Duramente          |  43 |   1 | 0.939 | 1 | 0.995 | 0.895 |
| Rhein Kraft        |  31 |   3 | 0.975 | 1 | 0.995 | 0.799 |
| Cesario            |  37 |   1 | 0.947 | 1 | 0.995 | 0.796 |
| Air Messiah        |  23 |   1 | 0.964 | 1 | 0.995 | 0.927 |
| Daring Heart       |  28 |   0 | 0.961 | 1 | 0.995 | 0.858 |
| Orfevre            |  25 |   3 | 0.947 | 1 | 0.995 | 0.995 |
| Gentildonna        |  40 |   1 | 0.944 | 1 | 0.995 | 0.597 |
| Win Variation      |  21 |   2 | 0.94 | 1 | 0.995 | 0.895 |
| Venus Paques       |  37 |   2 | 0.935 | 1 | 0.995 | 0.796 |
| Rigantona          |  28 |   1 | 0.995 | 1 | 0.995 | 0.91 |
| Sonon Elfie        |  29 |   1 | 0.994 | 1 | 0.995 | 0.815 |
