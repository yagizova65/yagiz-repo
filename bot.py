import random

# El işi fikirleri veritabanı (örnek)
fikirler = {
    "pet şişe": [
        {
            "isim": "Mini Saksı",
            "malzemeler": ["Pet şişe", "Makas", "Boya", "Toprak", "Bitki"],
            "adımlar": [
                "Pet şişenin alt kısmını kesin.",
                "Dış yüzeyini dilediğiniz renkte boyayın.",
                "İçine biraz toprak koyun ve bitkinizi dikin.",
            ]
        },
        {
            "isim": "Kuş Yemliği",
            "malzemeler": ["Pet şişe", "Makas", "Tahta çubuk", "Kuş yemi", "İp"],
            "adımlar": [
                "Şişenin yan tarafına birkaç delik açın.",
                "Deliklerden tahta çubukları geçirerek tünek yapın.",
                "İçine yem doldurun ve ip yardımıyla ağaca asın.",
            ]
        },
    ],
    "plastik kapak": [
        {
            "isim": "Renkli Mozaik Tablo",
            "malzemeler": ["Plastik kapaklar", "Karton", "Yapıştırıcı", "Boya (isteğe bağlı)"],
            "adımlar": [
                "Karton üzerine bir desen çizin.",
                "Kapakları desene göre yerleştirin.",
                "Yapıştırıcı ile sabitleyin.",
            ]
        },
        {
            "isim": "Eğitici Sayı Oyunu",
            "malzemeler": ["Kapaklar", "Kalem", "Karton"],
            "adımlar": [
                "Kapakların üzerine sayılar yazın.",
                "Kartona eşleşen sayı yuvaları açın.",
                "Çocuklar kapakları doğru yerlere yerleştirsin!",
            ]
        },
    ],
    "deterjan şişesi": [
        {
            "isim": "Kalemlik",
            "malzemeler": ["Boş deterjan şişesi", "Makas", "Boya"],
            "adımlar": [
                "Şişenin üst kısmını dikkatlice kesin.",
                "Kenarları düzeltin ve dışını boyayın.",
                "Masanız için kullanışlı bir kalemlik hazır!",
            ]
        }
    ]
}

def fikir_getir(plastik_turu):
    """Girilen plastik türüne göre fikir döndürür."""
    if plastik_turu in fikirler:
        secenekler = fikirler[plastik_turu]
        fikir = random.choice(secenekler)
        return fikir
    else:
        return None


def main():
    print("👋 PlastiKreatif'e Hoş Geldin! Evde plastiklerle neler yapabileceğini keşfedelim.")
    while True:
        plastik_turu = input("\nElinde hangi tür plastik var? (örn: pet şişe, plastik kapak, deterjan şişesi)\n> ").lower().strip()
        
        if plastik_turu in ["çık", "q", "exit"]:
            print("♻️ Görüşmek üzere! Unutma: Geri dönüşüm gelecektir!")
            break
        
        fikir = fikir_getir(plastik_turu)
        
        if fikir:
            print(f"\n🎨 Fikir: {fikir['isim']}")
            print(f"🧰 Malzemeler: {', '.join(fikir['malzemeler'])}")
            print("🪜 Adımlar:")
            for i, adim in enumerate(fikir['adımlar'], 1):
                print(f"  {i}. {adim}")
        else:
            print("😕 Bu plastik türü için şu anda fikrim yok. Başka bir şey dene!")
        

if __name__ == "__main__":
    main()
