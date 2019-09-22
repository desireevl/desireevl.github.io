---
layout: default
title: Slides
permalink: "/slides/"
---


<div class="home">
  <ul class="article-list">
    {% for post in site.pages %}
      {% if post.layout == 'slide' and post.title %}
        <li class="article-list-item {% if site.scrollappear_enabled %}scrollappear{% endif %}">
        <a href="{{ post.url | relative_url }}" title="{{ post.title }}">
          <h5>
            {{ post.title }}
            {% include svg-icon.html icon="arrow-right" %}
          </h5>
        </a>
        <p>
          {% if post.description %}
            {{ post.description }}  
          {% else %}
            {{ post.excerpt }}
          {% endif %}
        </p>
        <div class="article-list-footer">
          <span class="article-list-date">
            {{ post.date | date: "%B %-d, %Y" }}
          </span>
          <span class="article-list-divider">-</span>
          <span class="article-list-minutes">
            {% capture words %}
              {{ post.content | number_of_words }}
            {% endcapture %}
            {% unless words contains "-" %}
              {{ words | plus: 250 | divided_by: 250 | append: " minute read" }}
            {% endunless %}
          </span>
          <div class="article-list-tags">
            {% for tag in post.tags %}
              <a href="{{ 'tag/' | relative_url }}{{ tag }}">{{ tag }}</a>
            {% endfor %}
          </div>
        </div>
      </li>
      {% endif %}
    {% endfor %}
  </ul>
</div>