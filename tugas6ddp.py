{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNmp9P/nS7Wdkmse1WUx993"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":9,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"iRE4bfe4kvya","executionInfo":{"status":"ok","timestamp":1730449817199,"user_tz":-420,"elapsed":999,"user":{"displayName":"aditya sanjaya","userId":"04825243019981329985"}},"outputId":"d0bb2efe-9083-47f8-9bc0-badbeff085d3"},"outputs":[{"output_type":"stream","name":"stdout","text":["951 651 69 319 601 485 507 725 547 615 83 165 141 501 263 617 865 575 219 105 941 47 907 375 823 597 615 953 345 399 219 237 949 687 217 815 67 767 553 "]}],"source":["#print semua bilangan ganjil dari list berikut, hentikan perulangan ketika sudah melewati bilangan 553 pakai perulangan while\n","\n","numbers = [\n"," 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725,\n","547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390,\n","984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236,\n","375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,\n","918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815,\n","67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,\n","742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440,\n","380, 126, 721, 328, 753, 470, 743, 527\n","]\n","# print(numbers[0]\n","# print(len(numbers))\n","\n","index = 0\n","while index < len(numbers):\n","    angka = numbers[index]\n","    if angka % 2 == 1:\n","        print(angka, end=\" \")\n","    if angka == 553:\n","       break\n","    index += 1"]},{"cell_type":"code","source":["#buat lah output dari menggunakan bahasa pemprograman python dengan :\n","\n","#1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19 =\n","\n","hasil = 0\n","for a in range(1, 20, 2):\n","    hasil = hasil + a\n","print(f\"1+3+5+7+9+11+13+15+17+19 = {hasil}\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"HL5zAISk2Owp","executionInfo":{"status":"ok","timestamp":1730450623286,"user_tz":-420,"elapsed":395,"user":{"displayName":"aditya sanjaya","userId":"04825243019981329985"}},"outputId":"2fe7717e-11ab-493a-ab19-1d794c647989"},"execution_count":23,"outputs":[{"output_type":"stream","name":"stdout","text":["1+3+5+7+9+11+13+15+17+19 = 100\n"]}]},{"cell_type":"code","source":["#Buat program untuk minta input jumlah baris dan buatrangkaian berikut ini\n","#*\n","#**\n","#***\n","#****\n","#Dan seterusnya sejumlah baris yang diinputkan\n","#Gunakan for loop dengan range\n","\n","isUSer = int(input(\"Masukkan angka = \"))\n","for k in range(1, isUSer + 1):\n","    print(\"*\" * k)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"miZ-F3cV5Wt9","executionInfo":{"status":"ok","timestamp":1730451098185,"user_tz":-420,"elapsed":3015,"user":{"displayName":"aditya sanjaya","userId":"04825243019981329985"}},"outputId":"e0b55654-5055-4644-8c21-30392ffab210"},"execution_count":28,"outputs":[{"output_type":"stream","name":"stdout","text":["Masukkan angka = 5\n","*\n","**\n","***\n","****\n","*****\n"]}]}]}