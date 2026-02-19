# Dungeon Explorer - v3.0 Ereditarietà

Riprendiamo il Dungeon Explorer che avete già realizzato e lo estendiamo usando l'**ereditarietà**.

Il giocatore potrà scegliere un tipo di personaggio, e sulla mappa appariranno oggetti con effetti diversi.

---

## Nuove Regole

### Tipi di Personaggio

All'inizio della partita, dopo aver inserito il nome, il giocatore sceglie il tipo di personaggio:

| Tipo | Punti Vita | Attributo Speciale | Simbolo |
|:----:|:----------:|:------------------:|:-------:|
| Guerriero | 120 | Forza (10) | `G` |
| Mago | 80 | Mana (50) | `M` |
| Ladro | 100 | Agilità (15) | `L` |

Tutti i personaggi condividono: nome, posizione e punti vita. Ogni tipo ha un attributo esclusivo.

### Oggetti sulla Mappa

La mappa non è più vuota! All'inizio della partita vengono piazzati in posizioni casuali:

| Oggetto | Simbolo | Effetto |
|:-------:|:-------:|:--------|
| Pozione | `+` | Cura il giocatore (recupera punti vita) |
| Trappola | `X` | Danneggia il giocatore (toglie punti vita) |

Quando il giocatore entra in una cella con un oggetto:
- Se è una **Pozione**: recupera punti vita e l'oggetto scompare
- Se è una **Trappola**: perde punti vita e l'oggetto scompare
- In entrambi i casi viene stampato un messaggio con l'effetto

### Sconfitta

Se i punti vita del giocatore scendono a **0 o meno**, la partita termina con una sconfitta.

---

## Classi da Realizzare

### Gerarchia Giocatore

Partite dalla classe `Giocatore` che avete già scritto. Dovrete:

1. Aggiungere l'attributo `punti_vita` alla classe `Giocatore`
2. Creare tre classi figlie: `Guerriero`, `Mago`, `Ladro`
3. Ogni classe figlia:
   - Usa `super().__init__()` per inizializzare gli attributi del padre
   - Ha il proprio attributo speciale
   - Fa l'override di `__repr__()` per mostrare le informazioni specifiche del tipo

### Gerarchia Oggetto

Create una nuova gerarchia:

1. Classe padre `Oggetto` con attributi: `nome` e `simbolo`
2. Classe figlia `Pozione` con attributo: `punti_cura`
3. Classe figlia `Trappola` con attributo: `danno`
4. Ogni classe figlia usa `super().__init__()` e fa l'override di `__repr__()`

### Modifiche alle Classi Esistenti

- **Mappa**: deve piazzare gli oggetti in posizioni casuali e gestire la loro rimozione
- **DungeonExplorer**: deve mostrare il menu di scelta del personaggio e gestire l'interazione con gli oggetti usando `isinstance()`
- **Statistiche**: deve tracciare anche pozioni raccolte e trappole subite


## Consigli

Procedi per piccoli passi:

1. Aggiungi `punti_vita` a `Giocatore` e verifica che tutto funzioni come prima
2. Crea le tre classi figlie (`Guerriero`, `Mago`, `Ladro`) con `super()` e `__repr__()`
3. Crea la gerarchia `Oggetto` → `Pozione`, `Trappola`
4. Modifica `Mappa` per piazzare gli oggetti
5. Modifica `DungeonExplorer` per il menu di scelta e la gestione degli oggetti con `isinstance()`
6. Aggiungi la condizione di sconfitta (PV <= 0)
7. Aggiorna `Statistiche`

Happy coding!
10-Dungeon_Explorer_Ereditarieta.md
Visualizzazione di 10-Dungeon_Explorer_Ereditarieta.md.