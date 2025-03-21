import React, { useState } from 'react';

// 内联样式
const styles = {
  container: {
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '80px 20px',
  },
  header: {
    textAlign: 'center' as const,
    marginBottom: '64px',
  },
  gradientText: {
    background: 'linear-gradient(90deg, #4299E1, #805AD5)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    fontSize: '48px',
    fontWeight: 'bold',
  },
  subtitle: {
    fontSize: '20px',
    color: '#4A5568',
    maxWidth: '600px',
    margin: '20px auto',
  },
  buttonGroup: {
    display: 'flex',
    gap: '16px',
    justifyContent: 'center',
    marginTop: '32px',
  },
  primaryButton: {
    background: '#805AD5',
    color: 'white',
    padding: '12px 24px',
    borderRadius: '8px',
    border: 'none',
    cursor: 'pointer',
    fontSize: '16px',
    fontWeight: 'bold',
    transition: 'transform 0.2s',
    '&:hover': {
      transform: 'translateY(-2px)',
    },
  },
  secondaryButton: {
    background: 'transparent',
    color: '#805AD5',
    padding: '12px 24px',
    borderRadius: '8px',
    border: '2px solid #805AD5',
    cursor: 'pointer',
    fontSize: '16px',
    fontWeight: 'bold',
    transition: 'transform 0.2s',
  },
  featureGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
    gap: '32px',
    padding: '40px 0',
  },
  featureCard: {
    background: 'white',
    borderRadius: '12px',
    padding: '24px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
    transition: 'transform 0.3s',
    border: '1px solid #E2E8F0',
    '&:hover': {
      transform: 'translateY(-5px)',
    },
  },
  badge: {
    background: '#805AD5',
    color: 'white',
    padding: '4px 12px',
    borderRadius: '16px',
    fontSize: '14px',
    fontWeight: 'bold',
  },
  pricingSection: {
    background: '#F7FAFC',
    padding: '80px 0',
  },
  pricingGrid: {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
    gap: '32px',
    maxWidth: '1200px',
    margin: '0 auto',
    padding: '0 20px',
  },
  pricingCard: {
    background: 'white',
    borderRadius: '12px',
    padding: '32px',
    boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
    position: 'relative' as const,
  },
  popularBadge: {
    position: 'absolute' as const,
    top: '-12px',
    right: '-12px',
    background: '#805AD5',
    color: 'white',
    padding: '4px 12px',
    borderRadius: '16px',
    fontSize: '14px',
    fontWeight: 'bold',
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
  },
  demoNav: {
    display: 'flex',
    gap: '16px',
    justifyContent: 'center',
    marginBottom: '24px',
  },
  demoButton: {
    background: 'transparent',
    color: '#805AD5',
    padding: '12px 24px',
    borderRadius: '8px',
    border: '2px solid #805AD5',
    cursor: 'pointer',
    fontSize: '16px',
    fontWeight: 'bold',
    transition: 'transform 0.2s',
  },
};

// 图标组件
const ShieldIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
  </svg>
);

const CpuIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <rect x="4" y="4" width="16" height="16" rx="2" ry="2" />
    <rect x="9" y="9" width="6" height="6" />
    <line x1="9" y1="1" x2="9" y2="4" />
    <line x1="15" y1="1" x2="15" y2="4" />
    <line x1="9" y1="20" x2="9" y2="23" />
    <line x1="15" y1="20" x2="15" y2="23" />
    <line x1="20" y1="9" x2="23" y2="9" />
    <line x1="20" y1="14" x2="23" y2="14" />
    <line x1="1" y1="9" x2="4" y2="9" />
    <line x1="1" y1="14" x2="4" y2="14" />
  </svg>
);

const ZapIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
  </svg>
);

const CodeIcon = () => (
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <polyline points="16 18 22 12 16 6" />
    <polyline points="8 6 2 12 8 18" />
  </svg>
);

export default function HomePage() {
  const [activeDemo, setActiveDemo] = useState('mcp');
  
  const handleTryFree = () => {
    window.open('https://github.com/jsongeek/jsongeek-pro', '_blank');
  };

  const handleViewDocs = () => {
    window.open('https://docs.jsongeek-pro.com', '_blank');
  };

  const handlePurchase = (tier: string) => {
    if (tier === 'free') {
      window.open('https://github.com/jsongeek/jsongeek-pro', '_blank');
    } else if (tier === 'pro') {
      window.open('https://buy.jsongeek-pro.com', '_blank');
    } else {
      window.open('mailto:jsongeekai@sina.com', '_blank');
    }
  };

  const handleDemoChange = (demo: string) => {
    setActiveDemo(demo);
  };

  const features = [
    {
      Icon: ShieldIcon,
      title: 'MCP协议验证',
      description: '业内首创的智能JSON验证框架，确保数据完整性和安全性',
      badge: '独家',
    },
    {
      Icon: CpuIcon,
      title: 'DeepSeek LLM集成',
      description: '深度语义理解和智能安全分析，提供专业级数据洞察',
      badge: '智能',
    },
    {
      Icon: ZapIcon,
      title: '极致性能',
      description: '处理速度<2秒/10MB，内存占用<500MB，验证准确率>99.9%',
      badge: '高效',
    },
    {
      Icon: CodeIcon,
      title: '开发者工具链',
      description: '完整的CI/CD支持，Git集成和自动化工具',
      badge: '专业',
    },
  ];

  const pricingTiers = [
    {
      name: '基础版',
      price: '免费',
      features: [
        'JSON基础验证',
        'Schema验证',
        '社区支持',
      ],
      buttonText: '立即下载',
      isPopular: false,
    },
    {
      name: '专业版',
      price: '¥9.99',
      period: '/用户/年',
      features: [
        '全部基础功能',
        'DeepSeek LLM集成',
        '高级安全分析',
        '性能监控',
        '开发者工具链',
        '5×8技术支持',
      ],
      buttonText: '立即购买',
      isPopular: true,
    },
    {
      name: '企业版',
      price: '联系销售',
      features: [
        '全部专业版功能',
        '私有部署',
        '定制开发',
        'SLA保障',
        '7×24专属支持',
      ],
      buttonText: '联系我们',
      isPopular: false,
      action: 'mailto:jsongeekai@sina.com',
    },
  ];

  return (
    <div>
      {/* Hero Section */}
      <div style={styles.container}>
        <div style={styles.header}>
          <h1 style={styles.gradientText}>JsonGeekAI Pro</h1>
          <p style={styles.subtitle}>
            智能JSON处理和验证工具，集成DeepSeek LLM和MCP协议
          </p>
          <div style={styles.buttonGroup}>
            <button 
              style={styles.primaryButton}
              onClick={handleTryFree}
            >
              免费试用
            </button>
            <button 
              style={styles.secondaryButton}
              onClick={handleViewDocs}
            >
              查看文档
            </button>
          </div>
        </div>

        {/* Features Section */}
        <div style={styles.featureGrid}>
          {features.map((feature, index) => (
            <div key={index} style={styles.featureCard}>
              <feature.Icon />
              <div style={{ marginTop: '16px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <h3 style={{ fontSize: '20px', fontWeight: 'bold' }}>{feature.title}</h3>
                  <span style={styles.badge}>{feature.badge}</span>
                </div>
                <p style={{ color: '#4A5568', marginTop: '8px' }}>{feature.description}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Pricing Section */}
        <div style={styles.pricingSection}>
          <h2 style={{ textAlign: 'center', fontSize: '36px', marginBottom: '40px' }}>价格方案</h2>
          <div style={styles.pricingGrid}>
            {pricingTiers.map((tier, index) => (
              <div key={index} style={styles.pricingCard}>
                {tier.isPopular && <span style={styles.popularBadge}>最受欢迎</span>}
                <h3 style={{ fontSize: '24px', fontWeight: 'bold' }}>{tier.name}</h3>
                <div style={{ display: 'flex', alignItems: 'baseline', marginTop: '16px' }}>
                  <span style={{ fontSize: '36px', fontWeight: 'bold' }}>{tier.price}</span>
                  {tier.period && (
                    <span style={{ color: '#718096', marginLeft: '4px' }}>{tier.period}</span>
                  )}
                </div>
                <ul style={{ margin: '24px 0', paddingLeft: '20px' }}>
                  {tier.features.map((feature, i) => (
                    <li key={i} style={{ margin: '8px 0' }}>✓ {feature}</li>
                  ))}
                </ul>
                <button
                  style={{
                    ...styles.primaryButton,
                    width: '100%',
                    background: tier.isPopular ? '#805AD5' : 'transparent',
                    color: tier.isPopular ? 'white' : '#805AD5',
                    border: tier.isPopular ? 'none' : '2px solid #805AD5',
                    cursor: 'pointer',
                  }}
                  onClick={() => handlePurchase(tier.name === '基础版' ? 'free' : tier.name === '专业版' ? 'pro' : 'enterprise')}
                >
                  {tier.buttonText}
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Demo Section */}
        <div style={styles.demoSection}>
          <h2 style={{ textAlign: 'center', marginBottom: '24px' }}>快速上手</h2>
          <div style={styles.demoNav}>
            <button
              style={{
                ...styles.demoButton,
                background: activeDemo === 'mcp' ? '#805AD5' : 'transparent',
              }}
              onClick={() => handleDemoChange('mcp')}
            >
              MCP协议验证
            </button>
            <button
              style={{
                ...styles.demoButton,
                background: activeDemo === 'security' ? '#805AD5' : 'transparent',
              }}
              onClick={() => handleDemoChange('security')}
            >
              安全分析
            </button>
            <button
              style={{
                ...styles.demoButton,
                background: activeDemo === 'toolchain' ? '#805AD5' : 'transparent',
              }}
              onClick={() => handleDemoChange('toolchain')}
            >
              工具链
            </button>
          </div>
          <div style={styles.codeBlock}>
            {activeDemo === 'mcp' && (
              <>
                <div>$ pip install jsongeek-pro</div>
                <div style={{ marginTop: '16px' }}># MCP协议验证</div>
                <div>$ jsongeek validate data.json --mcp</div>
              </>
            )}
            {activeDemo === 'security' && (
              <>
                <div>$ pip install jsongeek-pro</div>
                <div style={{ marginTop: '16px' }}># 智能安全分析</div>
                <div>$ jsongeek validate api.json --security</div>
              </>
            )}
            {activeDemo === 'toolchain' && (
              <>
                <div>$ pip install jsongeek-pro</div>
                <div style={{ marginTop: '16px' }}># 工具链初始化</div>
                <div>$ jsongeek init toolchain</div>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
