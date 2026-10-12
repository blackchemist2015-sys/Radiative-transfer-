// Render an HTML file (with KaTeX math) to PDF using headless Chromium.
const { chromium } = require('playwright-core');
const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: process.env.CHROME });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(src), { waitUntil: 'load' });
  await page.waitForFunction(() => document.querySelectorAll('.katex').length > 0 || !document.querySelector('.math'), null, { timeout: 60000 });
  await page.waitForTimeout(1500);
  const errs = await page.evaluate(() => document.querySelectorAll('.katex-error').length);
  if (errs) console.error('KaTeX errors:', errs);
  await page.pdf({
    path: out, format: 'A4', printBackground: true,
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-size:8px;width:100%;text-align:center;color:#777">Radiative Transfer — <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
  });
  await browser.close();
})();
