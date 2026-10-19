// Build app/index.html: render equations to MathML (KaTeX) and inline the physics core + tables.
const fs = require('fs'), path = require('path');
const katex = require(process.env.KATEX || path.join(__dirname, '..', 'build', 'node', 'node_modules', 'katex'));
const src = fs.readFileSync(path.join(__dirname, 'src.html'), 'utf8');
const tex = {};
const re = /id: '(L\d+)'[\s\S]*?eq: String\.raw`([\s\S]*?)`/g;
let m;
while ((m = re.exec(src))) tex[m[1]] = katex.renderToString(m[2], { output: 'mathml', displayMode: true, throwOnError: true });
const out = src
  .replace('/*RTMATH*/', () => fs.readFileSync(path.join(__dirname, 'rtmath.js'), 'utf8'))
  .replace('/*TABLES*/', () => fs.readFileSync(path.join(__dirname, 'tables.json'), 'utf8'))
  .replace('/*TEXMAP*/', () => JSON.stringify(tex));
fs.writeFileSync(path.join(__dirname, 'index.html'), out);
console.log('wrote app/index.html,', (out.length / 1024).toFixed(0), 'kB,', Object.keys(tex).length, 'equations');
