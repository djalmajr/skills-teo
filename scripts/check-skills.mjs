import { readdirSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const root = 'skills';
const dirs = readdirSync(root, { withFileTypes: true })
  .filter((d) => d.isDirectory())
  .map((d) => d.name)
  .sort();

const missing = dirs.filter((n) => !existsSync(join(root, n, 'SKILL.md')));
if (missing.length) {
  console.error('missing SKILL.md:', missing.join(', '));
  process.exit(1);
}

const sj = JSON.parse(readFileSync('skills.json', 'utf8'));
const listed = [...new Set(sj.skills.flatMap((g) => g.skills || []))].sort();
const a = dirs.join(',');
const b = listed.join(',');
if (a !== b) {
  console.error('skills.json mismatch');
  console.error('dirs:', a);
  console.error('json:', b);
  process.exit(1);
}

for (const n of dirs) {
  const t = readFileSync(join(root, n, 'SKILL.md'), 'utf8');
  if (!t.startsWith('---')) {
    console.error(`${n}: missing frontmatter`);
    process.exit(1);
  }
  const m = t.match(/^---\n([\s\S]*?)\n---/);
  const name = (m?.[1].match(/^name:\s*(.+)$/m) || [])[1]?.trim();
  if (name !== n) {
    console.error(`${n}: frontmatter name mismatch:`, name);
    process.exit(1);
  }
}

console.log('ok', dirs.length, 'skills');
