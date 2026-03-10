# Genius Three-Layer Memory System v2.0

天才级永不失忆的 AI Agent 记忆系统。

## 核心能力

🧠 **记忆炼金师 + 首席思考官**
- 矛盾检测与解决
- 因果链提取（5-10条）
- 模式与洞见（8-15条智慧）
- 关系图谱维护
- 记忆评分（0-100分）
- 主动唤醒机制
- 自进化能力

## 三层架构

1. **Hourly Micro-Sync** (每2小时，9-23点)
   - 重要性评分 >70 才写入
   - 自动打分标签

2. **Daily Memory Sync** (每晚 21:00)
   - 捕获当天所有对话
   - 结构化日志

3. **Weekly Genius Compound** (每周日 22:00)
   - 7步深度工作
   - 矛盾检测、因果链、模式发现
   - 图谱更新、评分、精华提取、教训总结

## 文件结构

```
workspace/
├── MEMORY.md              # 长期精华（高密度）
├── INSIGHTS.md            # 每周洞见与智慧
├── RELATIONSHIPS.md       # 知识图谱（Markdown表格）
└── memory/
    └── YYYY-MM-DD.md     # 每日日志（带评分）
```

## 快速开始

### 1. 创建文件结构
```bash
mkdir memory
```

创建三个核心文件（可用空模板）：
- INSIGHTS.md
- RELATIONSHIPS.md  
- memory/2026-03-10.md

### 2. 添加 Cron Jobs
```bash
openclaw cron add < cron-daily.json
openclaw cron add < cron-weekly.json
openclaw cron add < cron-hourly.json
```

### 3. 更新 AGENTS.md
添加主动唤醒规则（见下方）

### 4. 初始化索引
```bash
openclaw memory index
```

## 主动唤醒机制

在 AGENTS.md 中添加：

```markdown
### ⚡ Proactive Memory Recall (GENIUS MODE)

每次回答用户问题前：
1. 提取关键词
2. 运行: openclaw memory search "<keywords>"
3. 检查 INSIGHTS.md 和 RELATIONSHIPS.md
4. 前缀回答: "根据我 [时间] 的洞见..."
```

## 使用

```bash
# 搜索记忆
openclaw memory search "项目进展"

# 查看状态
openclaw memory status

# 手动索引
openclaw memory index
```

## 效果

- ✅ 零失忆
- ✅ 记忆复利增长
- ✅ 主动唤醒相关记忆
- ✅ 持续自我进化

---

**版本**: v2.0 Genius  
**更新**: 2026-03-10
