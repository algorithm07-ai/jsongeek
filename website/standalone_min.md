import React, { useState } from 'react';

const commonStyles = {
  button: {
    padding: '12px 24px',
    borderRadius: '8px',
    cursor: 'pointer',
    fontSize: '16px',
    fontWeight: 'bold',
    transition: 'transform 0.2s',
  },
  card: {
    background: 'white',
    borderRadius: '12px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
  }
};

const styles = {
  container: { maxWidth: '1200px', margin: '0 auto', padding: '80px 20px' },
  header: { textAlign: 'center' as const, marginBottom: '64px' },
  gradientText: {
    background: 'linear-gradient(90deg, #4299E1, #805AD5)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    fontSize: '48px',
    fontWeight: 'bold',
  },
  subtitle: { fontSize: '20px', color: '#4A5568', maxWidth: '600px', margin: '20px auto' },
  buttonGroup: { display: 'flex', gap: '16px', justifyContent: 'center', marginTop: '32px' },
  primaryButton: {
    ...commonStyles.button,
    background: '#805AD5',
    color: 'white',
    border: 'none',
  },
  secondaryButton: {
    ...commonStyles.button,
    background: 'transparent',
    color: '#805AD5',
    border: '2px solid #805AD5',
  },
  featureGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
    gap: '32px',
    padding: '40px 0',
  },
  featureCard: {
    ...commonStyles.card,
    padding: '24px',
    transition: 'transform 0.3s',
    border: '1px solid #E2E8F0',
  },
  badge: {
    background: '#805AD5',
    color: 'white',
    padding: '4px 12px',
    borderRadius: '16px',
    fontSize: '14px',
    fontWeight: 'bold',
  },
  pricingSection: { background: '#F7FAFC', padding: '80px 0' },
  pricingGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
    gap: '32px',
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '0 20px',
  },
  pricingCard: {
    ...commonStyles.card,
    padding: '32px',
    position: 'relative' as const,
  },
  demoSection: {
    background: '#2D3748',
    color: 'white',
    padding: '40px 20px',
    borderRadius: '12px',
    fontFamily: 'monospace',
    maxWidth: '800px',
    margin: '40px auto',
  },
  codeBlock: {
    background: '#1A202C',
    padding: '20px',
    borderRadius: '8px',
    marginTop: '20px',
    lineHeight: '1.5',
  }
};

const Icon = ({ d }) => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <path d={d} />
  </svg>
);

export default function HomePage() {
  const [activeDemo, setActiveDemo] = useState('mcp');
  
  const handleAction = (url) => window.open(url, '_blank');
  
  const features = [
    {
      icon: "M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z",
      title: 'MCP协议验证',
      description: '业内首创的智能JSON验证框架',
      badge: '独家',
    },
    {
      icon: "M4 4h16v16H4z",
      title: 'DeepSeek LLM集成',
      description: '深度语义理解和智能安全分析',
      badge: '智能',
    },
    {
      icon: "M13 2L3 14h9l-1 8 10-12h-9z",
      title: '极致性能',
      description: '处理速度<2秒/10MB，准确率>99.9%',
      badge: '高效',
    },
    {
      icon: "M16 18l6-6-6-6M8 6l-6 6 6 6",
      title: '开发者工具链',
      description: '完整的CI/CD支持和自动化工具',
      badge: '专业',
    }
  ];

  const pricingTiers = [
    {
      name: '基础版',
      price: '免费',
      features: ['JSON基础验证', 'Schema验证', '社区支持'],
      action: 'https://github.com/jsongeek/jsongeek-pro',
    },
    {
      name: '专业版',
      price: '¥9.99',
      period: '/用户/年',
      features: ['全部基础功能', 'DeepSeek LLM集成', '高级安全分析', '性能监控', '开发者工具链', '5×8技术支持'],
      action: 'https://buy.jsongeek-pro.com',
      isPopular: true,
    },
    {
      name: '企业版',
      price: '联系销售',
      features: ['全部专业版功能', '私有部署', '定制开发', 'SLA保障', '7×24专属支持'],
      action: 'mailto:jsongeekai@sina.com',
    }
  ];

  const demos = {
    mcp: ['$ pip install jsongeek-pro', '# MCP协议验证', '$ jsongeek validate data.json --mcp'],
    security: ['$ pip install jsongeek-pro', '# 智能安全分析', '$ jsongeek validate api.json --security'],
    toolchain: ['$ pip install jsongeek-pro', '# 工具链初始化', '$ jsongeek init toolchain']
  };

  return (
    <div>
      <div style={styles.container}>
        <div style={styles.header}>
          <h1 style={styles.gradientText}>JsonGeekAI Pro</h1>
          <p style={styles.subtitle}>智能JSON处理和验证工具，集成DeepSeek LLM和MCP协议</p>
          <div style={styles.buttonGroup}>
            <button style={styles.primaryButton} onClick={() => handleAction('https://github.com/jsongeek/jsongeek-pro')}>免费试用</button>
            <button style={styles.secondaryButton} onClick={() => handleAction('https://docs.jsongeek-pro.com')}>查看文档</button>
          </div>
        </div>

        <div style={styles.featureGrid}>
          {features.map((f, i) => (
            <div key={i} style={styles.featureCard}>
              <Icon d={f.icon} />
              <div style={{ marginTop: '16px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <h3 style={{ fontSize: '20px', fontWeight: 'bold' }}>{f.title}</h3>
                  <span style={styles.badge}>{f.badge}</span>
                </div>
                <p style={{ color: '#4A5568', marginTop: '8px' }}>{f.description}</p>
              </div>
            </div>
          ))}
        </div>

        <div style={styles.pricingSection}>
          <h2 style={{ textAlign: 'center', fontSize: '36px', marginBottom: '40px' }}>价格方案</h2>
          <div style={styles.pricingGrid}>
            {pricingTiers.map((t, i) => (
              <div key={i} style={styles.pricingCard}>
                {t.isPopular && <span style={styles.badge}>最受欢迎</span>}
                <h3 style={{ fontSize: '24px', fontWeight: 'bold' }}>{t.name}</h3>
                <div style={{ display: 'flex', alignItems: 'baseline', marginTop: '16px' }}>
                  <span style={{ fontSize: '36px', fontWeight: 'bold' }}>{t.price}</span>
                  {t.period && <span style={{ color: '#718096', marginLeft: '4px' }}>{t.period}</span>}
                </div>
                <ul style={{ margin: '24px 0', paddingLeft: '20px' }}>
                  {t.features.map((f, i) => <li key={i} style={{ margin: '8px 0' }}>✓ {f}</li>)}
                </ul>
                <button style={{...styles.primaryButton, width: '100%'}} onClick={() => handleAction(t.action)}>
                  {t.name === '基础版' ? '立即下载' : t.name === '专业版' ? '立即购买' : '联系我们'}
                </button>
              </div>
            ))}
          </div>
        </div>

        <div style={styles.demoSection}>
          <h2 style={{ textAlign: 'center', marginBottom: '24px' }}>快速上手</h2>
          <div style={{ display: 'flex', gap: '16px', justifyContent: 'center', marginBottom: '24px' }}>
            {Object.keys(demos).map(k => (
              <button key={k} style={{
                ...styles.secondaryButton,
                background: activeDemo === k ? '#805AD5' : 'transparent',
                color: activeDemo === k ? 'white' : '#805AD5'
              }} onClick={() => setActiveDemo(k)}>
                {k === 'mcp' ? 'MCP协议验证' : k === 'security' ? '安全分析' : '工具链'}
              </button>
            ))}
          </div>
          <div style={styles.codeBlock}>
            {demos[activeDemo].map((line, i) => (
              <div key={i} style={i > 0 ? { marginTop: '16px' } : undefined}>{line}</div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
