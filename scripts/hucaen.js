console.log('Hucaen Module | Hello World!');

import { compilePack } from "@foundryvtt/foundryvtt-cli";
import { promises as fs } from "fs";
import path from "path";

const packs = await fs.readdir(path.join("src", "packs"));
for (const pack of packs) {
  if (pack === ".gitattributes") continue;
  if (pack === ".DS_Store") continue;
  console.log("Hucaen Module | Packing " + pack);
  const src = path.join("src", "packs", pack);
  const dest = path.join("packs", pack);
  await compilePack(src, dest, {
    log: true
  });
  console.log("Hucaen Module | Packed " + pack);
}