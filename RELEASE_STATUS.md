# Release scope

This release candidate publishes the parser-v4 task source snapshot and the
validated Windows and Linux runtime archives. It is a versioned software/data
snapshot, not a statement that all planned experiments have finished.

The code passes 55 offline tests in the packaging environment. Earlier native
checks cover representative task/seed/model combinations across the 11 task
families; the two physics tasks additionally have checks for their six published
seeds. These do not establish every task × seed × model combination or
Windows/Linux score equivalence. Linux Vulkan rendering has also been exercised
in the separate CUDA and LightWar campaigns. See release_connectivity_scope.json
for the original representative-check scope.

The supporting CSVs remain the audited export included in parser-v4. In
particular, computational_physics_episodes.csv predates the later parser
replacement campaign and parameter repeats. Do not describe that CSV as all
new V3/parser-v4 runs. Model-provider outages remain unscored, not model FAILs.

The original runtime ZIP/tar.gz and their hashes are preserved. Source changes
for this publication are limited to download documentation, hosting metadata,
license/notice copies and the downloader/statistics utilities. The original
task implementations, tests, parameters and numeric CSV bytes are unchanged.

The publisher's full per-scene asset-provenance inventory remains to be
completed. The existing project terms and third-party terms continue to apply;
this repository does not add a new license grant for third-party assets.
