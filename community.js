(() => {
  'use strict';
  const english = document.documentElement.lang === 'en';
  const translate = (zh, en) => english ? en : zh;
  const menus = [...document.querySelectorAll('.community-menu')];
  document.addEventListener('click', event => {
    menus.forEach(menu => { if (!menu.contains(event.target)) menu.open = false; });
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') menus.forEach(menu => {
      if (menu.open) { menu.open = false; menu.querySelector('summary').focus(); }
    });
  });
  menus.forEach(menu => menu.addEventListener('toggle', () => {
    if (menu.open) menus.filter(other => other !== menu).forEach(other => { other.open = false; });
  }));

  const form = document.querySelector('#game-submission');
  let submission = '';
  if (form) {
    const preview = document.querySelector('#submission-preview');
    const status = document.querySelector('#submission-status');
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const values = new FormData(form);
      const value = name => String(values.get(name) || '').trim();
      const title = value('game-title');
      const sections = [
        [translate('游戏或项目名称', 'Game or project title'), title],
        [translate('简单介绍', 'Short description'), value('description')],
        [translate('交互方式与操作', 'Interaction and controls'), value('interaction')],
        [translate('设备与平台', 'Hardware and platform'), value('hardware')],
        [translate('官方项目或论文链接', 'Primary source'), value('source-url')],
        [translate('配图来源', 'Image source'), value('image-url')],
        [translate('图片署名与授权', 'Image credit and rights'), value('image-credit')],
        [translate('贡献者署名', 'Contribution credit'), value('credit-handle') ? '@' + value('credit-handle') : '']
      ];
      submission = sections.filter(([, text]) => text).map(([heading, text]) => `### ${heading}\n${text}`).join('\n\n');
      document.querySelector('#submission-markdown').textContent = submission;
      const url = new URL('https://github.com/sharkburger/eyeTrackingGame_OpenDataBase/issues/new');
      url.searchParams.set('title', '[Game] ' + title);
      url.searchParams.set('body', submission);
      if (url.href.length > 7500) {
        url.searchParams.delete('body');
        status.textContent = translate('请复制投稿内容，在 GitHub 编辑框中粘贴并确认提交。', 'Copy your submission, then paste it into the GitHub editor to review and publish.');
      } else {
        status.textContent = translate('内容已准备好，可前往 GitHub 确认提交。', 'Your contribution is ready to review on GitHub.');
      }
      document.querySelector('#github-submission').href = url.href;
      preview.hidden = false;
      preview.focus();
      preview.scrollIntoView({ block: 'start', behavior: 'smooth' });
    });
    document.querySelector('#copy-submission').addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(submission);
        status.textContent = translate('投稿内容已复制。', 'Submission copied.');
      } catch {
        status.textContent = translate('请选择并复制上方预览内容。', 'Select and copy the preview above.');
      }
    });
    form.addEventListener('input', () => { preview.hidden = true; });
  }

  const credits = document.querySelector('#contributors-grid');
  if (credits) {
    const roles = {
      maintenance: translate('项目维护', 'Project maintenance'),
      data: translate('数据整理', 'Catalog data'),
      translation: translate('翻译', 'Translation'),
      code: translate('网站开发', 'Website development'),
      design: translate('设计', 'Design'),
      review: translate('来源审核', 'Source review'),
      documentation: translate('文档', 'Documentation'),
      accessibility: translate('无障碍改进', 'Accessibility')
    };
    fetch((english ? '../' : '') + 'data/contributors.json?v=20261016-source-images')
      .then(response => { if (!response.ok) throw new Error('credits'); return response.json(); })
      .then(data => {
        const cards = data.contributors.filter(person => /^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$/.test(person.github)).map(person => {
          const card = document.createElement('a');
          card.className = 'contributor-card';
          card.href = 'https://github.com/' + encodeURIComponent(person.github);
          const initial = document.createElement('span'); initial.className = 'contributor-initial'; initial.textContent = person.github[0].toUpperCase();
          const name = document.createElement('strong'); name.textContent = '@' + person.github;
          const role = document.createElement('span'); role.textContent = person.roles.map(key => roles[key] || key).join(' · ');
          card.append(initial, name, role);
          return card;
        });
        if (cards.length) credits.replaceChildren(...cards);
      })
      .catch(() => { /* The maintainer credit remains visible while the file loads. */ });
  }
})();
