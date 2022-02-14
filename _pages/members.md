---
layout: single
permalink: /members/
---

<style>
.container{width: 100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}
@media (min-width:576px){
.col-sm{position:relative;width:100%;min-height:1px;padding-right:15px;padding-left:15px;-ms-flex-preferred-size:0;flex-basis:0;-webkit-box-flex:1;-ms-flex-positive:1;flex-grow:1;max-width:100%}}
.row{display:-webkit-box;display:-ms-flexbox;display:flex;-ms-flex-wrap:wrap;flex-wrap:wrap;margin-right:-15px;margin-left:-15px}

</style>

CodeR-TSV is composed and represented by people from diverse genders, backgrounds, cultures and disciplines. We embrace and celebrate diversity in all its forms. CodeR-TSV is a space to learn and nurture a culture of curiosity, collaboration, interchange of ideas, troubleshooting, and sharing knowledge. Please see our [Statement of Philosophy](https://github.com/codertsv/GroupPolicies/blob/master/code-of-conduct.md) and [Code of Conduct](https://github.com/codertsv/GroupPolicies/blob/master/code-of-conduct.md)

<div class="container">
<div class="row">
<div class="col-sm">
<h2>Members</h2>


{% for member in site.data.members.organisers %}

<ul class="social-icons" style="list-style: none;">
    <li>
        <b>{{ member.name }}</b>
    </li>
    {% if member.twitter %}
    <li>
    <a style="text-decoration:none" href="https://twitter.com/{{ member.twitter }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-twitter-square" aria-hidden="true"></i><span class="label">Twitter</span>
    </a>
    {% endif %}
    {% if member.github %}
    <a style="text-decoration:none" href="https://github.com/{{ member.github }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-github" aria-hidden="true"></i>
        <span class="label">GitHub</span>
    </a>
    </li>
    {% endif %}
</ul>
{% endfor %}

</div>

  
<div class="col-sm">
<h2>Organising committee</h2>


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
    {% endif %}
    {% if member.github %}
    <a style="text-decoration:none" href="https://github.com/{{ member.github }}" rel="nofollow noopener noreferrer">
        <i class="fab fa-fw fa-github" aria-hidden="true"></i>
        <span class="label">GitHub</span>
    </a>
    </li>
    {% endif %}
</ul>
{% endfor %}

</div>
</div>
</div>
