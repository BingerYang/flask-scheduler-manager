# API文档

## SchedulerManager类

### 初始化

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_scheduler_manager import SchedulerManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduler.db'
db = SQLAlchemy(app)

scheduler_manager = SchedulerManager(app, db)
```

### 方法

#### `init_db()`
初始化数据库表。

```python
with app.app_context():
    scheduler_manager.init_db()
```

#### `add_job(job_id, func, trigger='cron', enabled=True, name=None, description=None, **kwargs)`
添加定时任务。

**参数：**
- `job_id` (str): 任务唯一标识
- `func` (str): 任务函数路径，格式：`module:function`
- `trigger` (str): 触发器类型，可选值：`cron`、`interval`、`date`
- `enabled` (bool): 是否启用，默认True
- `name` (str): 任务名称
- `description` (str): 任务描述
- `**kwargs`: 触发器参数和其他任务参数

**Cron触发器参数：**
- `year`, `month`, `day`, `week`, `day_of_week`, `hour`, `minute`, `second`
- `start_date`, `end_date`

**Interval触发器参数：**
- `weeks`, `days`, `hours`, `minutes`, `seconds`
- `start_date`, `end_date`

**Date触发器参数：**
- `start_date` 或 `run_date`

**其他参数：**
- `args`: 位置参数列表
- `kwargs`: 关键字参数字典
- `max_instances`: 最大并发实例数
- `misfire_grace_time`: 错过执行时间容忍度（秒）

**示例：**
```python
# Cron任务：每天10:30执行
scheduler_manager.add_job(
    job_id='daily_task',
    func='my_module:my_function',
    trigger='cron',
    hour=10,
    minute=30
)

# Interval任务：每5分钟执行
scheduler_manager.add_job(
    job_id='interval_task',
    func='my_module:my_function',
    trigger='interval',
    minutes=5
)

# 带参数的任务
scheduler_manager.add_job(
    job_id='task_with_args',
    func='my_module:my_function',
    trigger='interval',
    seconds=10,
    args=['arg1', 'arg2'],
    kwargs={'key': 'value'}
)
```

#### `get_job(job_id)`
获取任务。

**参数：**
- `job_id` (str): 任务ID

**返回：**
- `ScheduledJob`对象或None

#### `get_all_jobs(enabled_only=False)`
获取所有任务。

**参数：**
- `enabled_only` (bool): 是否只返回启用的任务

**返回：**
- 任务列表

#### `update_job(job_id, **kwargs)`
更新任务。

**参数：**
- `job_id` (str): 任务ID
- `**kwargs`: 要更新的字段

**返回：**
- 更新后的任务模型

#### `enable_job(job_id)`
启用任务。

**参数：**
- `job_id` (str): 任务ID

**返回：**
- `bool`: 是否成功

#### `disable_job(job_id)`
禁用任务。

**参数：**
- `job_id` (str): 任务ID

**返回：**
- `bool`: 是否成功

#### `remove_job(job_id)`
删除任务。

**参数：**
- `job_id` (str): 任务ID

**返回：**
- `bool`: 是否成功

#### `run_job(job_id)`
立即执行任务。

**参数：**
- `job_id` (str): 任务ID

**返回：**
- `bool`: 是否成功

#### `get_job_status(job_id)`
获取任务状态。

**参数：**
- `job_id` (str): 任务ID

**返回：**
- 状态字典，包含：
  - `job_id`: 任务ID
  - `enabled`: 是否启用
  - `next_run_time`: 下次执行时间
  - `last_run_time`: 上次执行时间
  - `scheduler_enabled`: 调度器中是否启用

## 数据库迁移

### `migrate_database(app, db)`
一键数据库迁移。

```python
from flask_scheduler_manager.migrations import migrate_database

with app.app_context():
    migrate_database(app, db)
```

### `reset_database(app, db)`
重置数据库（删除所有表并重新创建）。

```python
from flask_scheduler_manager.migrations import reset_database

with app.app_context():
    reset_database(app, db)
```

