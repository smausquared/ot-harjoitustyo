läpikäytävä koodi:
def main():
    kone = Machine()
    kone.drive()

```mermaid
sequenceDiagram
participant main
participant kone
participant moottori
participant bensatankki

main ->> kone: Machine()
kone ->> bensatankki: FuelTank()
kone ->> bensatankki: self._tank.fill(40)
kone ->> moottori: Engine(self._tank)
moottori ->> bensatankki: moottori.fuel_tank
main ->> kone: drive()
kone ->> moottori: moottori.start()
moottori ->> bensatankki: bensatankki.consume(5)
kone ->> moottori: moottori.is_running()
moottori -->> kone: True
kone ->> moottori: moottori.use_energy()
moottori ->> bensatankki: bensatankki.consume(10)
