# Untrusted Files

- Allow only file formats required by the business contract. Treat names,
  extensions, media types, signatures, metadata, and content as untrusted.
- Enforce upload count, compressed and expanded size, parser complexity,
  processing time, and storage limits before expensive work.
- Validate the extension, declared type, signature, and decoded structure with
  maintained format-aware parsers. No single signal proves the file type.
- Generate the storage name. Keep the original name as validated display
  metadata only. Do not use it as a filesystem or executable path.
- Store content outside executable and directly public locations. Authorize
  every later read, replacement, transform, and deletion.
- Scan, decode and re-encode, or isolate content when the assessed risk and
  format support that control. Reject archives with unsafe paths or expansion.

Example—store a bounded image as private content:

```text
upload → byte limit → allowlisted signature → maintained decoder
       → safe re-encode → generated object ID → private object store
```

The original filename remains display metadata. Downloads pass through an
authorized application boundary.

Source: pinned OWASP [File Upload Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/File_Upload_Cheat_Sheet.md).
