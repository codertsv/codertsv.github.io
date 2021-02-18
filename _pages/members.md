---
layout: single
permalink: /members/
---

CodeR-TSV is composed and represented by people from diverse genders, backgrounds, cultures and disciplines. We embrace and celebrate diversity in all its forms. CodeR-TSV is a space to learn and nurture a culture of curiosity, collaboration, interchange of ideas, troubleshooting, and sharing knowledge. Please see our [Statement of Philosophy](https://github.com/codertsv/GroupPolicies/blob/master/code-of-conduct.md) and [Code of Conduct](https://github.com/codertsv/GroupPolicies/blob/master/code-of-conduct.md)

## Members


{% for member in site.data.members.members %}
<ul class="social-icons" style="list-style: none;">
    <li>
        <b>{{ member.name }}</b>
    </li>
    {% if member.twitter %}
    <li>
    <a style="text-decoration:none" href="https://twitter.com/{{ member.twitter }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-twitter-square" aria-hidden="true"></i><span class="label">Twitter</span>
    </a>
    </li>
    {% endif %}
    {% if member.github %}
    <li>
    <a style="text-decoration:none" href="https://github.com/{{ member.github }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-github" aria-hidden="true"></i>
        <span class="label">GitHub</span>
    </a>
    </li>
    {% endif %}
</ul>
{% endfor %}

  
## Organising committee


{% for member in site.data.members.organisers %}
<ul class="social-icons" style="list-style: none;">
    <li>
        <b>{{ member.name }}</b>
    </li>
    {% if member.twitter %}
    <a style="text-decoration:none" href="https://twitter.com/{{ member.twitter }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-twitter-square" aria-hidden="true"></i><span class="label">Twitter</span>
    </a>
    {% endif %}
    {% if member.github %}
    <a style="text-decoration:none" href="https://github.com/{{ member.github }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-github" aria-hidden="true"></i>
        <span class="label">GitHub</span>
    </a>
    {% endif %}
</ul>
{% endfor %}
