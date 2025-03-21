// JsonGeekAI Pro Landing Page
const page=document.createElement('div');
page.innerHTML=`
<div class="container">
  <header>
    <h1>JsonGeekAI Pro</h1>
    <p>智能JSON处理和验证工具，集成DeepSeek LLM和MCP协议</p>
    <div class="buttons">
      <button onclick="window.open('https://github.com/jsongeek/jsongeek-pro')">免费试用</button>
      <button onclick="window.open('https://docs.jsongeek-pro.com')">查看文档</button>
    </div>
  </header>
  
  <div class="features">
    <div class="feature">
      <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      <h3>MCP协议验证</h3>
      <p>业内首创的智能JSON验证框架</p>
    </div>
    <div class="feature">
      <svg viewBox="0 0 24 24"><path d="M4 4h16v16H4z"/></svg>
      <h3>DeepSeek LLM集成</h3>
      <p>深度语义理解和智能安全分析</p>
    </div>
    <div class="feature">
      <svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9z"/></svg>
      <h3>极致性能</h3>
      <p>处理速度<2秒/10MB，准确率>99.9%</p>
    </div>
    <div class="feature">
      <svg viewBox="0 0 24 24"><path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/></svg>
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
        <button onclick="window.open('https://github.com/jsongeek/jsongeek-pro')">立即下载</button>
      </div>
      <div class="plan popular">
        <h3>专业版</h3>
        <div class="price">¥9.99<span>/用户/年</span></div>
        <ul>
          <li>全部基础功能</li>
          <li>DeepSeek LLM集成</li>
          <li>高级安全分析</li>
          <li>性能监控</li>
          <li>开发者工具链</li>
          <li>5×8技术支持</li>
        </ul>
        <button onclick="window.open('https://buy.jsongeek-pro.com')">立即购买</button>
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
        <button onclick="window.open('mailto:jsongeekai@sina.com')">联系我们</button>
      </div>
    </div>
  </div>

  <div class="demo">
    <h2>快速上手</h2>
    <div class="code">
      <pre>$ pip install jsongeek-pro
# MCP协议验证
$ jsongeek validate data.json --mcp</pre>
    </div>
  </div>
</div>
`;

// Styles
document.head.innerHTML += `
<style>
.container{max-width:1200px;margin:0 auto;padding:80px 20px}
header{text-align:center;margin-bottom:64px}
h1{background:linear-gradient(90deg,#4299E1,#805AD5);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:48px}
.buttons{display:flex;gap:16px;justify-content:center;margin-top:32px}
button{padding:12px 24px;border-radius:8px;cursor:pointer;font-weight:700}
.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:32px;padding:40px 0}
.feature{background:#fff;padding:24px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,.1)}
.pricing{background:#F7FAFC;padding:80px 0}
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:32px}
.plan{background:#fff;padding:32px;border-radius:12px;box-shadow:0 4px 6px rgba(0,0,0,.1)}
.demo{background:#2D3748;color:#fff;padding:40px;border-radius:12px;margin:40px auto;max-width:800px}
.code{background:#1A202C;padding:20px;border-radius:8px;margin-top:20px}
</style>
`;
