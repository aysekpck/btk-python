#Regular Expression:
"""dağınık bir metin içerisinde istediğimiz formattaki metinleri yakalayabilmemize imkan tanır.
Mesela, bir kaynakta geçen tüm e-posta adreslerini veya içinde rakam bulunan ve gmail uzantılı olan mail adreslerini ayıklamak için kullanabilirsiniz.
Düzenli ifadeler olmasaydı ardı arkasına birçok if - else yazmak gerekebilirdi.
Bu modül, birkaç saatte yapabileceğiniz bir işlemi saniyeler içerisinde sizin yerinize yapabiliyor
"""

import re
cumle="ayşe çok güzel bir kızdır.Ayrıca çok zeki"
print(re.findall("çok",cumle)) #cümlede bulur
print(re.findall("nem",cumle))#yok ise boş köşeli parantez çıkarır

"^" işareti, belirtilen karakterle başlıyor mu? ona bakar
"$" belirtilen karakterle bitiyor mu?
"*" bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
"+" bir karakterin bir ya da daha fazla ol. kontrol eder.
"?" sıfır ya da bir kere ol. kontrol eder.
"{}" karakter sayısını kontrol eder.



print(re.findall("^a",cumle))

print(re.findall("a*yşe",cumle))

print(re.findall("çok{1}",cumle))


print(re.split(" ",cumle)) #boşluktan itibaren ayırdı
print(re.split("l",cumle)) #l'yi göstermeden l den itibaren ayırır

print(re.sub(" ","-",cumle)) #boşluğu kısa çizgi ile değiştirdi

print(re.search("çok",cumle))#<re.Match object; span=(5, 8), match='çok'> #cümlede arar

print(re.match("çok",cumle)) #cümlenin başı "ço"k ile mi başlıyor sorar
#aynısını split metotuyla da yaparız ve daha hızlı çalışır.



