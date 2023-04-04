```mermaid
sequenceDiagram
participant main
participant laitehallinto
participant rautatietori
participant ratikka6
participant bussi244
participant lippu_luukku
participant kallen_kortti

main ->> laitehallinto: HKLLaitehallinto()
main ->> rautatietori: Lataajalaite()
main ->> ratikka6: Lukijalaite()
main ->> bussi244: Lukijalaite()

main ->> laitehallinto: laitehallinto.lisaa_lataaja(rautatietori)
laitehallinto -->> rautatietori: laitehallinto.lataajat.append(rautatietori) 
main ->> laitehallinto: laitehallinto.lisaa_lukija(ratikka6)
laitehallinto -->> ratikka6: laitehallinto.lukijat.append(ratikka6)
main ->> laitehallinto: laitehallinto.lisaa_lukija(bussi244)
laitehallinto -->> ratikka6: laitehallinto.lukijat.append(bussi244)
main ->> lippu_luukku: Kioski()
lippu_luukku ->> kallen_kortti: lippu_luukku.osta_matkakortti("Kalle")
lippu_luukku ->> uusi_kortti: Matkakortti("Kalle")
uusi_kortti -->> lippu_luukku: uusi_kortti
lippu_luukku -->> kallen_kortti: uusi_kortti
main ->> rautatietori: rautatietori.lataa_arvoa(kallen_kortti, 3)
rautatietori ->> kallen_kortti: kallen_kortti.kasvata_arvoa(3)
main ->> ratikka6: ratikka6.osta_lippu(kallen_kortti, 0)
ratikka6 -->> kallen_kortti: kallen_kortti.arvo < hinta
kallen_kortti -->> ratikka6: False
ratikka6 ->> kallen_kortti: kallen_kortti._vahenna_arvoa(hinta)

main ->> bussi244: bussi244.osta_lippu(kallen_kortti,2)
bussi244 -->> kallen_kortti: kallen_kortti.arvo < hinta
kallen_kortti -->> bussi244: True
bussi244 -->> main: False