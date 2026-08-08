# Systemarchitektur

## Ziele und Annahmen

Das System unterstützt zunächst einen Nutzer und einen Architektur-Agenten,
läuft lokal, verarbeitet überwiegend Markdown und soll nachvollziehbare
technische Empfehlungen liefern. Vorrang haben Korrektheit, Provenienz,
Korrekturrechte und einfache Wiederherstellung; extreme Skalierung ist kein
MVP-Ziel.

## Schichten

1. **Run State:** aktueller Kontext und Checkpoints; nicht automatisch dauerhaft.
2. **Episodic Log:** verdichtete Sitzungen mit Entscheidungen, Aktionen,
   Ergebnissen und offenen Punkten.
3. **Personal Memory:** stabile Präferenzen, Projekte und Constraints, strikt
   nach Nutzer und Datenschutzklasse getrennt.
4. **Knowledge Wiki:** Quellen, Konzepte, Muster, Cases und Synthesen.
5. **Derived Indexes:** Volltext, Embeddings und Beziehungen; vollständig
   löschbar und aus Git rekonstruierbar.

## Write Path

```text
Chat/Quelle -> unveränderter Eingang -> Extraktion -> Inbox
           -> Schema- und Policy-Prüfung -> menschliche Freigabe
           -> kanonische Seite -> Compile/Lint -> abgeleitete Indizes
```

Automatische Extraktion erzeugt Kandidaten, keine Wahrheit. Eine Promotion
benötigt Seitentyp, stabile ID, Provenienz, Datenschutzklasse, Konfidenz,
Zeitbezug und Review-Datum. Änderungen an bestehendem Wissen werden als
Korrektur, Ergänzung oder Widerspruch modelliert.

## Read Path

1. Anfrage klassifizieren und Scope bestimmen.
2. Deterministisch nach Nutzer, Projekt, Datenschutz, Status und Zeit filtern.
3. Kandidaten parallel über Links/IDs, Volltext und Embeddings abrufen.
4. Rankings per Reciprocal Rank Fusion zusammenführen.
5. Kleine Kandidatenmenge optional reranken.
6. Quellenabschnitte laden, Antwort erzeugen und Claim-zu-Quelle-Bezug prüfen.
7. Retrieval-Trace ohne unnötige private Inhalte protokollieren.

Vektorsuche ist damit ein Recall-Kanal, nicht der Wahrheitsrichter.

## Datenmodell

Pflichtfelder stehen in `schemas/page.schema.json`. Wesentliche Relationen:

- `supports`, `contradicts`, `supersedes` für Claims;
- `applies_to`, `depends_on`, `evaluated_by` für Architekturwissen;
- `derived_from` für Synthesen;
- `reviewed_at`, `valid_from`, `valid_until` für zeitliche Gültigkeit.

Jede Löschung entfernt die kanonische Seite oder das erlaubte Feld, baut alle
Projektionen neu und prüft anschließend mit einem Negativtest, dass der Inhalt
nicht mehr abrufbar ist.

## Failure Boundaries und Erkennung

- **Falsche Promotion:** Inbox/Freigabe und Audit-Log.
- **Stale Knowledge:** Review-Datum, Quellen-Freshness und Stale-Report.
- **Widersprüche:** explizite Kanten und Contradiction-Report.
- **Retrieval Leakage:** ACL vor semantischer Suche, Tenant-Negativtests.
- **Index Drift:** Index-Manifest mit Modell, Dimensionen, Chunker und Hash;
  Änderungen erzwingen einen vollständigen Rebuild.
- **Halluzinierte Provenienz:** nur existierende IDs/Abschnitte zitierbar;
  Antwort-Claims werden gegen geladene Quellen geprüft.
- **Agentische Selbstmutation:** keine automatische Änderung von Policies,
  Prompts oder Skills ohne Eval, Review, Canary und Rollback.

## Betrieb

Jeder Build validiert JSON Schema, tote Links, doppelte IDs, fehlende Quellen,
Widersprüche, veraltete Seiten und Datenschutzmarkierungen. Git liefert Review,
Diff und Rollback. Backups müssen Repository und private Rohquellen getrennt
abdecken; abgeleitete Indizes brauchen kein eigenes Backup.

Telemetry umfasst Query-Klasse, Filter, Kandidaten-IDs, Ranks, Latenzen,
Tokenkosten, verwendete Quellen und Nutzerfeedback. Prompts oder Inhalte werden
nur gemäß Datenschutzklasse erfasst.
