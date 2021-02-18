---
layout: single
permalink: /members/
---

CodeR-TSV is composed and represented by people from diverse genders, backgrounds, cultures and disciplines. We embrace and celebrate diversity in all its forms. CodeR-TSV is a space to learn and nurture a culture of curiosity, collaboration, interchange of ideas, troubleshooting, and sharing knowledge. Please see our [Statement of Philosophy](https://github.com/codertsv/GroupPolicies/blob/master/code-of-conduct.md) and [Code of Conduct](https://github.com/codertsv/GroupPolicies/blob/master/code-of-conduct.md)

## Members

<ul class="author__urls social-icons">
{% for member in site.data.members.members %}
    <li>
        <b>{{ member.name }}</b>
    </li>
    {% if member.twitter %}
    <li>
    <a href="https://twitter.com/{{ member.twitter }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-twitter-square" aria-hidden="true"></i><span class="label">Twitter</span>
    </a>
    </li>
    {% endif %}
    {% if member.github %}
    <li>
    <a href="https://github.com/{{ member.github }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-github" aria-hidden="true"></i>
        <span class="label">GitHub</span>
    </a>
    </li>
    {% endif %}
{% endfor %}
</ul>
  
## Organising committee

<ul class="author__urls social-icons">
{% for member in site.data.members.organisers %}
    <li>
        <b>{{ member.name }}</b>
    </li>
    {% if member.twitter %}
    <li>
    <a href="https://twitter.com/{{ member.twitter }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-twitter-square" aria-hidden="true"></i><span class="label">Twitter</span>
    </a>
    </li>
    {% endif %}
    {% if member.github %}
    <li>
    <a href="https://github.com/{{ member.github }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-github" aria-hidden="true"></i>
        <span class="label">GitHub</span>
    </a>
    </li>
    {% endif %}
{% endfor %}
</ul>