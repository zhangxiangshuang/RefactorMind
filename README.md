# RefactorMind 

**RefactorMind** 是一个基于多智能体（Multi-Agent）协同的 AI 驱动代码重构系统。它旨在解决传统人工代码审查与重构效率低、标准不一、难以规模化落地的痛点，通过“感知-决策-执行”的三层架构，实现从代码异味检测到自动化测试验证的全流程闭环。

##  核心特性

- ** 多Agent协同架构**：采用 Orchestrator（调度）、CodeParser（解析）、Planning（规划）、Refactor（重构）、Verifier（验证）等多角色智能体分工协作，模拟真实开发团队的作业模式。
- ** 长链推理决策**：规划 Agent 结合架构规范与代码上下文进行 Chain-of-Thought (CoT) 推理，生成安全、可追溯的重构路径，并自动附带影响分析与回滚预案。
- **️ 安全闭环验证**：重构 Agent 自动生成 Pull Request 并补全单元测试，Verifier Agent 触发 CI 流水线进行自动化验证，确保重构不引入新缺陷。
- ** 企业级落地成果**：已在 20 人规模的后端团队常态化运行，代码规范评估通过率提升 **80%**，单次重构平均耗时从 4 小时降至 **45 分钟**。

## ️ 系统架构

系统采用分层设计，确保各模块职责清晰、扩展性强：

1. **感知层 (Perception)**：利用 AST（抽象语法树）解析与语义嵌入技术，精准识别代码中的坏味道（Code Smells）和技术债。
2. **决策层 (Decision)**：规划 Agent 结合历史上下文，生成多条重构路径并评估置信度，选择最优方案。
3. **执行层 (Execution)**：重构 Agent 编写高质量代码，测试 Agent 补全单元测试，Verifier Agent 负责最终的 CI/CD 闭环。

## ️ 技术栈

- **核心框架**：Python, LangChain
- **AI 模型**：GPT-4 / Claude 3 / **Xiaomi MiMo** (正在接入评测)
- **代码分析**：Tree-sitter, AST
- **工程化集成**：GitHub Actions, Docker, GitLab API

##  快速开始

### 环境准备
确保你的环境中已安装 Python 3.9+ 以及对应的依赖包。

```bash
git clone https://github.com/zhangxiangshuang/RefactorMind.git
cd RefactorMind
pip install -r requirements.txt
