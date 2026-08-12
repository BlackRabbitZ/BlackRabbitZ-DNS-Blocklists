# Migration to v3.3.2

This release integrates the extended lists **by function** into the existing BlackRabbitZ sections. The README no longer separates them by source.

On the first workflow run after upgrading, the repository automatically:

1. Removes legacy source-prefixed files under `lists/special/hagezi-*.txt` and `lists/ips/hagezi-*.txt`.
2. Rebuilds the extended lists under neutral BlackRabbitZ functional names in `lists/categories/` and `lists/ips/`.
3. Publishes large Security, Family, Ultimate, NRD/DGA and other extended lists with a maximum of **50 MiB per part**.
4. Refreshes `README.md` and `README_EN.md` with current entry counts, Raw links and part tables where required.
5. Keeps HaGeZi provenance in generated file headers and in `THIRD_PARTY.md` / `ATTRIBUTION.md`.

## Important

After pushing the upgrade, let the **Update blocklists** workflow finish completely, then use **Fetch origin** in GitHub Desktop before making more local changes.
