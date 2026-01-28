# Oracle PowerPoint Template Layout Mapping

Quick reference for selecting appropriate slide layouts.

## Dark Template (51 slides, 0-indexed: 0-50)

### Themed Slides

| Slide | Type | Description | Use When |
|-------|------|-------------|----------|
| 0 | Cover | Master brand/OCI/Database title | Opening slide, presentation title |
| 1 | Speaker | Single speaker (virtual) | 1 speaker with headshot |
| 2 | Speaker Profile | Speaker with experience/expertise/location | Detailed speaker bio |
| 3 | Speakers | 2 speakers (virtual) | 2 speakers with headshots |
| 4 | Speakers | 3 speakers (virtual) | 3 speakers with headshots |
| 5 | Speakers | 4 speakers (virtual) | 4 speakers with headshots |
| 6 | Speakers | 6 speakers (virtual) | 6 speakers with headshots |
| 7-8 | Section Divider | Section break slides | Starting new topic/section |
| 9-10 | Impact Statement | Bold message slide | Key takeaway or impact message |
| 11 | Thank You | Closing slide | End of presentation |
| 12 | Quote | Quote with attribution | Customer quote, testimonial |

### Standard Content Slides

| Slide | Type | Description | Use When |
|-------|------|-------------|----------|
| 13-15 | Title + Body | Title with bullet points | General content, lists, key points |
| 16-17 | Title + 3 Points | Title with 3 key points | Exactly 3 distinct concepts |
| 18 | Bold Statement | Large text, minimal content | Impact message, key stat |
| 19-22 | 2-Column | Title with 2 columns | Comparing 2 items, before/after |
| 23-25 | 3-Column | Title with 3 columns | Exactly 3 items or categories |
| 26-30 | Image + Text | Various photo/text combinations | Visual storytelling |
| 31-35 | Story Slides | Customer stories with images/stats | Case studies, testimonials |
| 36-40 | Statistics | Data-focused layouts | Numbers, metrics, KPIs |
| 41-50 | Abstract Backgrounds | Content with visual backgrounds | Modern, stylized slides |

## Light Template (55 slides, 0-indexed: 0-54)

### Themed Slides

| Slide | Type | Description | Use When |
|-------|------|-------------|----------|
| 0 | Cover | Master brand/OCI/Database title | Opening slide, presentation title |
| 1 | Speaker | Single speaker (virtual) | 1 speaker with headshot |
| 2 | Speaker Profile | Speaker with experience/expertise/location | Detailed speaker bio |
| 3 | Speakers | 2 speakers (virtual) | 2 speakers with headshots |
| 4 | Speakers | 3 speakers (virtual) | 3 speakers with headshots |
| 5 | Speakers | 4 speakers (virtual) | 4 speakers with headshots |
| 6 | Speakers | 6 speakers (virtual) | 6 speakers with headshots |
| 7-10 | Section Divider | Section break slides | Starting new topic/section |
| 11-12 | Impact Statement | Bold message slide | Key takeaway or impact message |
| 13 | Thank You | Closing slide | End of presentation |
| 14 | Quote | Quote with attribution | Customer quote, testimonial |

### Standard Content Slides

| Slide | Type | Description | Use When |
|-------|------|-------------|----------|
| 15-17 | Title + Body | Title with bullet points | General content, lists, key points |
| 18-19 | Title + 3 Points | Title with 3 key points | Exactly 3 distinct concepts |
| 20 | Bold Statement | Large text, minimal content | Impact message, key stat |
| 21-24 | 2-Column | Title with 2 columns | Comparing 2 items, before/after |
| 25-27 | 3-Column | Title with 3 columns | Exactly 3 items or categories |
| 28-32 | Image + Text | Various photo/text combinations | Visual storytelling |
| 33-37 | Story Slides | Customer stories with images/stats | Case studies, testimonials |
| 38-42 | Statistics | Data-focused layouts | Numbers, metrics, KPIs |
| 43-54 | Abstract Backgrounds | Content with visual backgrounds | Modern, stylized slides |

## Content Type Decision Tree

### 1. What type of content do you have?

**Opening/Title**:
- → Use slide 0 (Cover)

**Speakers**:
- 1 speaker → slide 1
- 2 speakers → slide 3
- 3 speakers → slide 4
- 4 speakers → slide 5
- 6 speakers → slide 6
- Speaker with detailed bio → slide 2

**Section Break**:
- → Use slides 7-8 (dark) or 7-10 (light)

**Bullet Points/List**:
- → Use slides 13-15 (Title + Body)

**Exactly 3 Key Points**:
- → Use slides 16-17 (Title + 3 Points)

**Exactly 2 Items to Compare**:
- → Use slides 19-22 (2-Column)

**Exactly 3 Items/Categories**:
- → Use slides 23-25 (3-Column)

**Image with Text**:
- → Use slides 26-30 (Image + Text)

**Customer Story/Case Study**:
- → Use slides 31-35 (Story Slides)

**Statistics/Numbers/Data**:
- → Use slides 36-40 (Statistics)

**Impact Message/Key Stat**:
- → Use slide 18 (Bold Statement) or 9-10 (Impact Statement)

**Quote/Testimonial**:
- → Use slide 12 (Quote)

**Closing**:
- → Use slide 11 (Thank You)

## Layout Selection Best Practices

### ✅ Do

- **Count your content first**: Before selecting a layout, count how many distinct items/concepts you have
- **Match placeholders to content**: Ensure every placeholder will be filled with meaningful content
- **Use appropriate layouts**: 2-column for 2 items, 3-column for 3 items, etc.
- **Break into multiple slides**: If you have too much content, split across slides
- **Consult inventories**: Check `dark-inventory.json` or `light-inventory.json` for exact shape details

### ❌ Don't

- **Force content into wrong layouts**: Don't use 3-column layout for 2 items
- **Leave placeholders empty**: Every placeholder should have content
- **Stack charts below text**: Use 2-column or full-slide layouts for charts/tables
- **Guess slide numbers**: Always use 0-indexed numbering (first slide = 0)

## Common Presentation Patterns

### Basic 5-Slide Presentation
```
Slide 0: Cover (slide 0)
Slide 1: Agenda (slide 13 - Title + Body)
Slide 2: Main Content (slide 13 - Title + Body)
Slide 3: Key Message (slide 18 - Bold Statement)
Slide 4: Thank You (slide 11)

Template mapping: 0,13,13,18,11
```

### Multi-Speaker Event (7 slides)
```
Slide 0: Cover (slide 0)
Slide 1: Speakers (slide 4 - 3 speakers)
Slide 2: Section Intro (slide 7)
Slide 3: Topic 1 (slide 13 - Title + Body)
Slide 4: Topic 2 (slide 19 - 2-Column)
Slide 5: Key Takeaway (slide 9 - Impact Statement)
Slide 6: Thank You (slide 11)

Template mapping: 0,4,7,13,19,9,11
```

### Customer Story (5 slides)
```
Slide 0: Cover (slide 0)
Slide 1: Challenge (slide 13 - Title + Body)
Slide 2: Solution (slide 26 - Image + Text)
Slide 3: Results (slide 36 - Statistics)
Slide 4: Quote (slide 12)
Slide 5: Thank You (slide 11)

Template mapping: 0,13,26,36,12,11
```

## Notes

- **Slide indexing**: All slides are 0-indexed (first slide = 0, not 1)
- **Duplication**: Same slide index can appear multiple times in template mapping
- **Theme differences**: Dark has 51 slides, Light has 55 slides
- **Speaker slides**: Use WITHOUT headshots for large live events, WITH headshots for virtual events
- **Hyperlinks on light slides**: Must manually change to Sky 120 (yellow) - not automated

For complete details on each layout, refer to the JSON inventory files:
- `dark-inventory.json` - Complete Dark template inventory
- `light-inventory.json` - Complete Light template inventory
