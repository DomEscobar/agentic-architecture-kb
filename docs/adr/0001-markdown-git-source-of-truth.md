# ADR-0001: Markdown und Git als Source of Truth

- Status: accepted
- Datum: 2026-08-08

## Kontext

Das Wiki muss durch Menschen lesbar, lokal betreibbar, überprüfbar, korrigierbar
und unabhängig von Embedding-Modellen oder Datenbankprodukten sein.

## Entscheidung

Kanonische Inhalte werden als Markdown mit validiertem YAML-Frontmatter in Git
gespeichert. Volltext-, Vektor- und Graphindizes sind abgeleitete Artefakte.

## Konsequenzen

Positiv: einfache Reviews, Diffs, Backups und Rollbacks; kein Lock-in; ein
defekter oder veralteter Index kann vollständig neu gebaut werden.

Negativ: konkurrierende Writer und sehr große Korpora benötigen später eine
Transaktionsschicht; Schemaänderungen brauchen Migrationen; Zugriffsrechte auf
Feldebene sind im Dateisystem begrenzt.

## Alternativen

- Postgres als Primärspeicher gewinnt bei vielen gleichzeitigen Schreibern und
  komplexen ACL-Abfragen.
- Ein Property Graph gewinnt bei häufigen, evaluierten Multi-Hop-Abfragen.
- Ein SaaS-Vector-Store gewinnt nur, wenn Betriebsentlastung wichtiger als
  lokale Kontrolle und Portabilität ist.
