
# Insertion Sort Algorithm

Basit bir liste tanımlayarak başlayalım.
Aşağıdaki gibi bir listemiz olsun:

22, 27, 16, 2, 18, 6

    - Yukarıdaki dizinin sort türüne göre aşamalarını yazalım.
    - [16, 22, 27, 2, 18, 6]
    - [2, 16, 22, 27, 18, 6]
    - [2, 16, 18, 22, 27, 6]
    - [2, 6, 16, 18, 22, 27]

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

Big-O notation gösterimini yapalım.
    
    - O(n^2)

Time Complexity değerini bulalım.

    - Best case: O(n) = O(36)
    - Worst case: O(n^2) = O(36)
    - Average case: O(n^2) = O(36)
    
Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer. Yazalım.

    - Average case kapsamına girer. Çünkü sıralama ne ilk adımda ne de son adımda tamamlandı.

Bir başka liste de şöyle olsun:

7, 3, 5, 8, 2, 9, 4, 15, 6

    - Yukarıdaki dizi için step by step Insertion Sort işlem adımları şöyledir:
    - [3, 7, 5, 8, 2, 9, 4, 15, 6]
    - [3, 5, 7, 8, 2, 9, 4, 15, 6]
    - [2, 3, 5, 7, 8, 9, 4, 15, 6]
    - [2, 3, 4, 5, 7, 8, 9, 15, 6]
