```html
<!doctype html>
<html lang="zh">
<head>
  <meta charset="UTF-8" />
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="JsonGeekAI Pro: 智能JSON处理和验证工具，集成DeepSeek LLM和MCP协议">
  <title>JsonGeekAI Pro</title>
  <script id="yourware-collect-script">
    (function(win, export_obj) {
      win['LogAnalyticsObject'] = export_obj;
      if (!win[export_obj]) {
        function _collect() {
          _collect.q.push(arguments);
        }
        _collect.q = _collect.q || [];
        win[export_obj] = _collect;
      }
      win[export_obj].l = +new Date();
    })(window, 'collectEvent');
  </script>
  <script async id="yourware-rangers-script" src="https://lf3-data.volccdn.com/obj/data-static/log-sdk/collect/5.0/collect-rangers-v5.1.12.js"></script>
  <script src="https://lib.yourware.so/yourware-lib.umd.js" id="yourware-lib" data-type="page"></script>
  <style>
    :root {
      --primary: #805AD5;
      --secondary: #4299E1;
      --text: #4A5568;
      --bg: #F7FAFC;
      --code: #1A202C;
    }
    * {margin: 0;padding: 0;box-sizing: border-box;}
    body {font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;}
    .container {max-width: 1200px;margin: 0 auto;padding: 80px 20px;}
    header {text-align: center;margin-bottom: 64px;}
    h1 {background: linear-gradient(90deg,var(--secondary),var(--primary));-webkit-background-clip: text;-webkit-text-fill-color: transparent;font-size: 48px;}
    .subtitle {font-size: 20px;color: var(--text);max-width: 600px;margin: 20px auto;}
    .buttons {display: flex;gap: 16px;justify-content: center;margin-top: 32px;}
    button {padding: 12px 24px;border-radius: 8px;cursor: pointer;font-weight: 700;font-size: 16px;}
    .primary {background: var(--primary);color: white;border: none;}
    .secondary {background: transparent;color: var(--primary);border: 2px solid var(--primary);}
    .features {display: grid;grid-template-columns: repeat(auto-fit,minmax(280px,1fr));gap: 32px;padding: 40px 0;}
    .feature {background: white;padding: 24px;border-radius: 12px;box-shadow: 0 4px 6px rgba(0,0,0,.1);cursor:pointer;transition:transform .2s;}
    .feature:hover {transform:translateY(-5px);}
    .feature svg {width: 24px;height: 24px;stroke: currentColor;}
    .feature h3 {font-size: 20px;margin: 16px 0 8px;}
    .feature p {color: var(--text);}
    .pricing {background: var(--bg);padding: 80px 0;}
    .pricing h2 {text-align: center;font-size: 36px;margin-bottom: 40px;}
    .plans {display: grid;grid-template-columns: repeat(auto-fit,minmax(300px,1fr));gap: 32px;max-width: 1200px;margin: 0 auto;padding: 0 20px;}
    .plan {background: white;padding: 32px;border-radius: 12px;box-shadow: 0 4px 6px rgba(0,0,0,.1);}
    .plan h3 {font-size: 24px;}
    .price {display: flex;align-items: baseline;margin: 16px 0;font-size: 36px;font-weight: 700;}
    .period {color: #718096;font-size: 16px;margin-left: 4px;}
    .plan ul {margin: 24px 0;padding-left: 20px;}
    .plan li {margin: 8px 0;}
    .demo {background: #2D3748;color: white;padding: 40px;border-radius: 12px;max-width: 800px;margin: 40px auto;}
    .demo h2 {text-align: center;margin-bottom: 24px;}
    .code {background: var(--code);padding: 20px;border-radius: 8px;margin-top: 20px;font-family: monospace;}
    .code div {margin-top: 16px;}
    .code div:first-child {margin-top: 0;}
  </style>
</head>
<body>
  <div id="root">
    <div class="container">
      <header>
        <h1>JsonGeekAI Pro</h1>
        <p class="subtitle">智能JSON处理和验证工具，集成DeepSeek LLM和MCP协议</p>
        <div class="buttons">
          <button class="primary" onclick="window.location.href='/download'">免费试用</button>
          <button class="secondary" onclick="window.location.href='/docs'">查看文档</button>
        </div>
      </header>

      <div class="features">
        <div class="feature" onclick="window.location.href='/docs#mcp'">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          <h3>MCP协议验证</h3>
          <p>业内首创的智能JSON验证框架</p>
        </div>
        <div class="feature" onclick="window.location.href='/docs#llm'">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M4 4h16v16H4z"/>
          </svg>
          <h3>DeepSeek LLM集成</h3>
          <p>深度语义理解和智能安全分析</p>
        </div>
        <div class="feature" onclick="window.location.href='/docs#performance'">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M13 2L3 14h9l-1 8 10-12h-9z"/>
          </svg>
          <h3>极致性能</h3>
          <p>处理速度<2秒/10MB，准确率>99.9%</p>
        </div>
        <div class="feature" onclick="window.location.href='/docs#toolchain'">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>
          </svg>
          <h3>开发者工具链</h3>
          <p>完整的CI/CD支持和自动化工具</p>
        </div>
      </div>

      <div class="pricing">
        <h2>价格方案</h2>
        <div class="plans">
          <div class="plan">
            <h3>基础版</h3>
            <div class="price">免费</div>
            <ul>
              <li>JSON基础验证</li>
              <li>Schema验证</li>
              <li>社区支持</li>
            </ul>
            <button class="primary" onclick="window.location.href='/download'">立即下载</button>
          </div>
          <div class="plan">
            <h3>专业版</h3>
            <div class="price">¥9.99<span class="period">/用户/年</span></div>
            <ul>
              <li>全部基础功能</li>
              <li>DeepSeek LLM集成</li>
              <li>高级安全分析</li>
              <li>性能监控</li>
              <li>开发者工具链</li>
              <li>5×8技术支持</li>
            </ul>
            <button class="primary" onclick="window.location.href='/pricing'">立即购买</button>
          </div>
          <div class="plan">
            <h3>企业版</h3>
            <div class="price">联系销售</div>
            <ul>
              <li>全部专业版功能</li>
              <li>私有部署</li>
              <li>定制开发</li>
              <li>SLA保障</li>
              <li>7×24专属支持</li>
            </ul>
            <button class="primary" onclick="window.location.href='/contact'">联系我们</button>
          </div>
        </div>
      </div>

      <div class="demo">
        <h2>快速上手</h2>
        <div class="buttons">
          <button class="secondary active" onclick="showDemo('mcp')">MCP协议验证</button>
          <button class="secondary" onclick="showDemo('security')">安全分析</button>
          <button class="secondary" onclick="showDemo('toolchain')">工具链</button>
        </div>
        <div class="code" id="demo-code">
          <div>$ pip install jsongeek-pro</div>
          <div># MCP协议验证</div>
          <div>$ jsongeek validate data.json --mcp</div>
        </div>
      </div>
    </div>
  </div>
  <script>
    function showDemo(type) {
      const demos = {
        mcp: ['$ pip install jsongeek-pro', '# MCP协议验证', '$ jsongeek validate data.json --mcp'],
        security: ['$ pip install jsongeek-pro', '# 智能安全分析', '$ jsongeek validate api.json --security'],
        toolchain: ['$ pip install jsongeek-pro', '# 工具链初始化', '$ jsongeek init toolchain']
      };
      const code = document.getElementById('demo-code');
      code.innerHTML = demos[type].map(line => `<div>${line}</div>`).join('');
      
      // Update button states
      document.querySelectorAll('.demo .secondary').forEach(btn => {
        const isActive = btn.textContent.includes({
          mcp: 'MCP',
          security: '安全',
          toolchain: '工具'
        }[type]);
        if (isActive) {
          btn.classList.add('active');
          btn.style.background = 'var(--primary)';
          btn.style.color = 'white';
        } else {
          btn.classList.remove('active');
          btn.style.background = 'transparent';
          btn.style.color = 'var(--primary)';
        }
      });
    }
  </script>
</body>
</html>
```
