import re

with open('d:/filosofia_experimental/unidad2-clase17.html', 'r', encoding='utf-8') as f:
    orig = f.read()

head_and_nav = orig.split('<!-- HERO -->')[0]
scripts_and_close = orig.split('</nav>')[-1] # after footer nav

# modify head_and_nav
head_and_nav = head_and_nav.replace('<title>La PCR: Tecnología, ADN y la Batalla contra el COVID | FILOSOFÍA&CIENCIA</title>', '<title>El Inductivismo: Bacon y el Pavo de Russell | FILOSOFÍA&CIENCIA</title>')
head_and_nav = head_and_nav.replace('<span>Unidad 2</span> · Clase 17', '<span>Unidad 3</span> · Clase 18')
head_and_nav = head_and_nav.replace("window.location.href='unidad2-clase16.html'", "window.location.href='unidad2-clase17.html'")
head_and_nav = head_and_nav.replace("Clase 16", "Clase 17")

# add hover scale to images
css_hover = '''
        /* Custom Hover for Images */
        .figure-img, .inline-img { transition: transform 0.5s cubic-bezier(0.4,0,0.2,1); }
        .figure:hover .figure-img, .inline-img:hover { transform: scale(1.08); z-index: 10; position: relative; }
'''
head_and_nav = head_and_nav.replace('</style>', css_hover + '    </style>')

html = head_and_nav + """<!-- HERO -->
<header id="art-hero" style="background:
    linear-gradient(to left, rgba(0,0,0,.15) 0%, rgba(0,0,0,.65) 32%, rgba(0,0,0,.97) 58%),
    url('Bacon.jpg') right top/auto 100% no-repeat,
    url('https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=1600&q=80') center/cover no-repeat;
    background-color: #000;">
    <div class="hero-breadcrumb">
        <span class="hero-badge">UNIDAD 3 · CLASE 18</span>
        <span class="hero-badge-outline">MÉTODOS</span>
    </div>
    <p class="hero-eyebrow">Filosofía e Historia de la Ciencia y la Tecnología · 6° Año</p>
    <h1 class="hero-title">
        El <em>Inductivismo</em>:<br>De la observación<br>a la ley general
    </h1>
    <p class="hero-subtitle">
        Cómo el método de Francis Bacon transformó la ciencia a partir de la acumulación de datos, y qué problemas esconde detrás de su aparente lógica perfecta.
    </p>
    <div class="hero-meta">
        <div class="hero-meta-item">
            <i class="fa-solid fa-user"></i>
            <span>Prof. Filosofía & Ciencia</span>
        </div>
        <div class="hero-meta-sep"></div>
        <div class="hero-meta-item">
            <i class="fa-solid fa-calendar"></i>
            <span>Ciclo 2025</span>
        </div>
        <div class="hero-meta-sep"></div>
        <div class="hero-meta-item">
            <i class="fa-solid fa-clock"></i>
            <span>60 min · Clase 18</span>
        </div>
        <div class="hero-meta-sep"></div>
        <div class="hero-meta-item">
            <i class="fa-solid fa-book-open"></i>
            <span>Bacon · Russell · Inducción</span>
        </div>
    </div>
    <div class="hero-scroll-cue">
        <div class="scroll-dot"></div>
        <span>Comenzar</span>
    </div>
</header>

<!-- ARTICLE BODY -->
<main class="article-wrap">

    <!-- ===================== MAIN CONTENT ===================== -->
    <article class="article-main">

        <!-- INTRO -->
        <div class="article-section reveal" id="sec-intro">
            <span class="section-label">Introducción</span>
            <h2 class="article-h2">El poder de la <span>observación</span></h2>
            <p class="article-p dropcap">
                Pensemos en cómo aprendemos las cosas más básicas del mundo. El fuego quema, el sol sale por el este, si suelto una manzana, cae al piso. ¿Cómo llegamos a esas conclusiones? Las descubrimos observando que sucedían una y otra vez. Jamás vimos a una manzana flotar hacia arriba, así que asumimos que la próxima vez que soltemos una manzana, también caerá.
            </p>
            <p class="article-p">
                Este mecanismo tan natural e intuitivo se llama <strong>razonamiento inductivo</strong>. Consiste en partir de observaciones particulares (datos empíricos individuales) y llegar a una conclusión general que abarque todos los casos. 
                Durante siglos, y especialmente a partir de la Revolución Científica del siglo XVII, este método se instituyó como la <strong>forma principal de construir conocimiento verdaderamente objetivo</strong> frente al saber derivado de los antiguos dogmas o la autoridad religiosa.
            </p>
        </div>

        <hr class="art-divider">

        <!-- BACON -->
        <div class="article-section reveal" id="sec-bacon">
            <span class="section-label">El Padre del Método Moderno</span>
            <h2 class="article-h2">Francis Bacon: Contra los <span>ídolos de la mente</span></h2>

            <div class="figure reveal">
                <img class="figure-img" style="height:auto;max-height:420px;object-fit:cover;border-radius:12px;"
                     src="Bacon.jpg"
                     alt="Retrato de Francis Bacon"
                     onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
                <div class="figure-img-placeholder" style="display:none;">📜</div>
                <div class="figure-caption">
                    <strong>Francis Bacon (1561–1626)</strong> Filósofo y estadista inglés.
                    Sistematizó empíricamente el método científico en su obra <em>Novum Organum</em>.
                </div>
            </div>

            <p class="article-p">
                En el siglo XVII, el universo intelectual europeo seguía dominado por los silogismos deductivos de Aristóteles. Básicamente, se discutía desde grandes axiomas universales dados por ciertos. <strong>Francis Bacon</strong> revolucionó esta estructura. En su libro <em>Novum Organum</em> (1620), propuso un nuevo instrumento ('órgano') para el pensamiento: invertir el proceso.
            </p>

            <div class="callout dark-box reveal">
                <div class="callout-tag">🧠 Los ídolos según Bacon</div>
                <div class="callout-title">Limpiar la mente para ver la verdad</div>
                <p>Bacon creía que para observar la naturaleza pura, sin prejuicios, el científico tenía que eliminar los "ídolos" de su mente:
                </p>
                <ul>
                    <li style="margin-bottom:8px;"><strong>Ídolos de la tribu:</strong> Los errores intrínsecos de la naturaleza humana, como confiar demasiado en los sentidos.</li>
                    <li style="margin-bottom:8px;"><strong>Ídolos de la caverna:</strong> Los prejuicios de cada individuo formados por su educación personal y su entorno único.</li>
                    <li style="margin-bottom:8px;"><strong>Ídolos del foro (o mercado):</strong> Las distorsiones e imprecisiones creadas por el lenguaje común.</li>
                    <li style="margin-bottom:8px;"><strong>Ídolos del teatro:</strong> Los dogmas falsos instaurados por sistemas filosóficos o religiones antiguas y aceptados como reales.</li>
                </ul>
            </div>

        </div>

        <hr class="art-divider">

        <!-- CÓMO FUNCIONA LA INDUCCIÓN -->
        <div class="article-section reveal" id="sec-metodo">
            <span class="section-label">Estructura Lógica</span>
            <h2 class="article-h2">¿Cómo funciona el <span>Inductivismo</span>?</h2>

            <p class="article-p">
                El argumento inductivista ingenuo o clásico sigue un proceso sistemático de acumular información:
            </p>

            <div class="pcr-steps reveal">
                <div class="pcr-step">
                    <div class="pcr-step-num">1</div>
                    <div class="pcr-step-name" style="color:#ef4444;">Observación Pura</div>
                    <div class="pcr-step-desc">
                        Se observan hechos individuales de la naturaleza de manera objetiva y meticulosa, usando los sentidos e instrumentos (microscopios o telescopios), sin sesgos o teorías previas.
                    </div>
                </div>
                <div class="pcr-step">
                    <div class="pcr-step-num" style="background:#f97316;">2</div>
                    <div class="pcr-step-name" style="color:#f97316;">Acumulación de Casos</div>
                    <div class="pcr-step-desc">
                        Se repiten las observaciones en diversas condiciones temporales y espaciales. Una sola observación no alcanza; se necesita una gran cantidad representativa de datos y ocurrencias.
                    </div>
                </div>
                <div class="pcr-step">
                    <div class="pcr-step-num" style="background:#22c55e;">3</div>
                    <div class="pcr-step-name" style="color:#22c55e;">Generalización (Inferencia)</div>
                    <div class="pcr-step-desc">
                        Tras observar que en todos los casos se repite un patrón, el científico realiza un "salto lógico" (inferencia inductiva) y formula verbal o matemáticamente una <strong>Ley General</strong>.
                    </div>
                </div>
            </div>

            <div class="pull-quote reveal">
                <p class="pull-quote-text">
                    "Si un gran número de <em>A</em> han sido observados bajo una amplia variedad de condiciones, y si todos esos <em>A</em> observados poseen sin excepción la propiedad <em>B</em>, entonces todos los <em>A</em> tienen la propiedad <em>B</em>."
                </p>
                <p class="pull-quote-author">— Principio Clásico de la Inducción</p>
            </div>
            
            <p class="article-p">
                Así descubrimos verdades científicas clásicas. Por ejemplo: afirmamos que "los metales se dilatan con el calor", porque luego de calentar repetidamente cobre, plata y oro en distintas condiciones alrededor del planeta, descubrimos que absolutamente todos sufrieron dilatación térmica.
            </p>
        </div>

        <hr class="art-divider">

        <!-- EL PROBLEMA: HUME Y RUSSELL -->
        <div class="article-section reveal" id="sec-hume">
            <span class="section-label">La Crítica Epistemológica</span>
            <h2 class="article-h2">El problema de la inducción y <span>el Pavo de Russell</span></h2>

            <p class="article-p">
                Pese al enorme éxito de la etapa científica moderna basada en la inducción, pronto emergió un problema muy serio en su estructura. En el siglo XVIII, el filósofo escocés empirista <strong>David Hume</strong> fue el primero en alertar que este método sufre de un problema lógico mortal: <em>ninguna cantidad finita de observaciones puede lógicamente obligarnos y autorizarnos a decretar una conclusión garantizada sobre el infinito total</em>.
            </p>
            <p class="article-p">
                Doscientos años después, el gran matemático <strong>Bertrand Russell</strong> propuso una analogía brillante conocida como la famosa historia de <strong>"El Pavo Inductivista"</strong> para evidenciar el gran "salto al vacío" de Hume.
            </p>

            <div class="figure reveal">
                <img class="figure-img" style="height:auto;max-height:480px;object-fit:cover;border-radius:12px;"
                     src="Russell.jpg"
                     alt="Retrato de Bertrand Russell"
                     onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
                <div class="figure-img-placeholder" style="display:none;">🦃</div>
                <div class="figure-caption">
                    <strong>Bertrand Russell (1872–1970)</strong> Matemático, filósofo y escritor británico. Usó la sátira del pavo para criticar duramente las expectativas ciegas de los teóricos y pensadores acerca de nuestra costumbre de asumir que "el universo del mañana tiene la obligación comportarse exactamente igual al de hoy".
                </div>
            </div>

            <div class="callout yellow reveal">
                <div class="callout-tag">🦃 La Parábola Epistemológica</div>
                <div class="callout-title">El Pavo Científico</div>
                <p>Imaginemos un pavo que vive en una granja y que aprendió y aplica a la perfección el método inductivista en todo su rigor.</p>
                <p>En su primer día de vida anotó cuidadosamente: <em>"Hoy me dieron de comer maíz a las 9 am."</em> Como buen inductivista, sabía que no debía sacar conclusiones por un solo suceso particular. Requirió tomar muchísimas más observaciones sistemáticamente. Día tras día anotaba las condiciones en su libreta: <em>"Me dieron de comer a las 9 am los días calurosos, me dieron maíz los martes fríos, me dieron maíz los días de tormenta..."</em></p>
                <p>Jamás existió una sola excepción durante todos esos meses de la granja. Así que luego de acumular suficiente base empírica repetitiva en una gran variedad de condiciones, el 23 de Diciembre realizó la inferencia lógica final para establecer su Ley Universal Inductiva final:</p>
                <p style="font-size:18px; text-align:center; font-family:'Playfair Display',serif; color:#000; margin: 15px 0;"><strong>"Siempre y en toda circunstancia se da de comer al pavo a las 9 am."</strong></p>
                <p>Lamentablemente para su rígida lógica irrefutable, el 24 de diciembre a las 9 am en lugar de maíz... se presentó el granjero y le cortó el cuello.</p>
            </div>

            <p class="article-p">
                Lo que Hume planteó teóricamente, y lo que demostró el Pavo empíricamente en carne propia, es que las justificaciones inductivistas de generalización se operan circularmente en lo que llamamos el dogma de la "homogeneidad de la naturaleza". Inducimos que las cosas seguirán comportándose así, por mera <strong>costumbre psicológica o animal</strong> de nuestra historia previa. El problema del método es que usa a la misma inducción como prueba para asegurar que la inducción funciona.
            </p>

            <div class="callout red reveal">
                <div class="callout-tag">🔢 La Matemática y la Falsa Inducción</div>
                <div class="callout-title">Un caso real numérico de engaño</div>
                <p>¿Qué pasa si evaluamos la expresión matemática <strong style="font-family:monospace">n² - n + 41</strong> usando inductivismo básico, incrementando <strong style="font-family:monospace">n</strong> una a una buscando un patrón general universal?</p>
                <p>Resultados:</p>
                <ul style="margin:8px 0 10px 20px;">
                    <li>n=1 → <span style="font-family:monospace">1 - 1 + 41 = 41</span> (Es Primo)</li>
                    <li>n=2 → <span style="font-family:monospace">4 - 2 + 41 = 43</span> (Es Primo)</li>
                    <li>n=3 → <span style="font-family:monospace">9 - 3 + 41 = 47</span> (Es Primo)</li>
                    <li>...</li>
                    <li>n=40 → (Es Primo)</li>
                </ul>
                <p>Un biólogo o físico inductivista viendo que repitió el experimento 40 veces distintas, induciría la ley matemática: "Todos los elementos naturales evaluados aquí otorgan matemáticamente un número primo".</p>
                <p>Pero ¿qué ocurre súbitamente en el elemento 41? Reemplacemos:<br><strong style="font-family:monospace">41² - 41 + 41 = 41² (o bien 1681)</strong><br>El resultado numérico termina siendo divisible por 41 exactos y ya no es un número primo, ¡y toda la maravillosa Ley universal inductivista colapsa y se despedaza con un único y minúsculo caso negativo!</p>
            </div>
            
        </div>

        <hr class="art-divider">

        <!-- DISCUSIÓN -->
        <div class="discussion-section reveal">
            <h3 class="discussion-title">🤔 Para pensar y debatir</h3>
            <ul class="question-list">
                <li class="question-item">
                    <div class="question-num">1</div>
                    <p class="question-text">Pensemos en los "Ídolos" de Bacon: ¿Es posible limpiar y purificar a la mente humana para que alcance una "observación absolutamente pura" despojada completamente de sus propios sesgos e hipótesis?</p>
                </li>
                <li class="question-item">
                    <div class="question-num">2</div>
                    <p class="question-text">Aún con su debilidad a que "falle el evento de un día para otro", ¿Por qué seguimos confiando en las generalizaciones inductivas todo el tiempo en nuestra sociedad?</p>
                </li>
                <li class="question-item">
                    <div class="question-num">3</div>
                    <p class="question-text">El famoso caso del Cisne Negro: los europeos deducían inductivamente que todos los cisnes eran blancos hasta el siglo 17 porque jamás vieron uno de otro color. Hasta que cruzaron a Australia y hallaron la mutación genética. ¿Creen que los paradigmas cambian a raíz de encontrar excepciones?</p>
                </li>
            </ul>
        </div>
    </article>

    <!-- ===================== SIDEBAR ===================== -->
    <aside class="article-sidebar">
        <div class="sidebar-sticky">

            <!-- TABLE OF CONTENTS -->
            <div class="sidebar-card">
                <div class="sidebar-card-header">
                    <i class="fa-solid fa-list"></i>
                    Contenido de la clase
                </div>
                <ul class="toc-list">
                    <li class="toc-item"><a href="#sec-intro" class="toc-link"><span class="toc-num">01</span> Observación</a></li>
                    <li class="toc-item"><a href="#sec-bacon" class="toc-link"><span class="toc-num">02</span> Francis Bacon</a></li>
                    <li class="toc-item"><a href="#sec-metodo" class="toc-link"><span class="toc-num">03</span> Estructura lógica</a></li>
                    <li class="toc-item"><a href="#sec-hume" class="toc-link"><span class="toc-num">04</span> Crítica al inductivismo</a></li>
                </ul>
            </div>

            <!-- CONCEPTS -->
            <div class="sidebar-card">
                <div class="sidebar-card-header">
                    <i class="fa-solid fa-key"></i>
                    Conceptos clave
                </div>
                <div class="concept-mini">
                    <div class="concept-mini-name">Inductivismo</div>
                    <div class="concept-mini-def">Método de inferencia desde una sumatoria de hechos o características particulares para justificar afirmaciones universales verdaderas.</div>
                </div>
                <div class="concept-mini">
                    <div class="concept-mini-name">Empirismo</div>
                    <div class="concept-mini-def">Corriente filosófica y marco natural de la ciencia que determina a la observación a los sentidos y la experimentación material como el centro del progreso para hallar conocimiento.</div>
                </div>
                <div class="concept-mini">
                    <div class="concept-mini-name">Inferencia Circular</div>
                    <div class="concept-mini-def">Error en el que las conclusiones que intentamos avalar se dan basándonos en la misma exactitud del postulado inicial buscando justificar una causa dentro del mismo patrón.</div>
                </div>
            </div>

            <!-- PHILOSOPHERS -->
            <div class="sidebar-card">
                <div class="sidebar-card-header">
                    <i class="fa-solid fa-user-graduate"></i>
                    Protagonistas
                </div>
                <div class="philosopher-card">
                    <div class="philosopher-avatar">📜</div>
                    <div>
                        <div class="philosopher-name">Francis Bacon</div>
                        <div class="philosopher-dates">1561 – 1626 · Inglaterra</div>
                        <div class="philosopher-bio">Propuso reorganizar radicalmente nuestra estructura mediante el empirismo y "purgar" al razonamiento de todos los «idolos o falsas creencias» instaurados por viejos engaños.</div>
                    </div>
                </div>
                <div class="philosopher-card">
                    <div class="philosopher-avatar">🤔</div>
                    <div>
                        <div class="philosopher-name">David Hume</div>
                        <div class="philosopher-dates">1711 – 1776 · Escocia</div>
                        <div class="philosopher-bio">Sostuvo que todo concepto inductivo que hacemos sobre el futuro asumiendo lo idéntico al pasado, recae enteramente al concepto animal primitivo humano de repetir un 'hábito'.</div>
                    </div>
                </div>
                <div class="philosopher-card">
                    <div class="philosopher-avatar">🦃</div>
                    <div>
                        <div class="philosopher-name">Bertrand Russell</div>
                        <div class="philosopher-dates">1872 – 1970 · Inglaterra</div>
                        <div class="philosopher-bio">Inminente premio Nobel inglés de literatura y matemática que diseñó el caso del pavo creyente de la ciencia al que en víspera de navidad, en vez de trigo se topa al final con su sentencia universal empírica.</div>
                    </div>
                </div>
            </div>

            <!-- PREV CLASS -->
            <div class="sidebar-card">
                <div class="sidebar-card-header">
                    <i class="fa-solid fa-backward"></i>
                    Clase anterior
                </div>
                <div class="next-class">
                    <div class="next-label">Clase 17 · Unidad 2</div>
                    <div class="next-title">La PCR: Copiar el ADN para salvar al mundo</div>
                    <button class="btn-next" onclick="window.location.href='unidad2-clase17.html'" style="background:var(--bg3);color:var(--text);">
                        <span>IR A CLASE 17</span>
                        <i class="fa-solid fa-arrow-left"></i>
                    </button>
                </div>
            </div>

        </div>
    </aside>

</main>

<!-- FOOTER NAV -->
<nav class="article-footer-nav" style="border-top:1px solid var(--border); padding: 40px 24px; max-width:1280px; margin:0 auto; display:flex; justify-content:space-between; flex-wrap:wrap; gap:20px;">
    <a href="unidad2-clase17.html" class="footer-nav-link prev" style="display:flex; align-items:center; gap:12px; padding:16px 24px; border-radius:16px; border:1px solid var(--border); background:var(--card); transition:all 0.3s; cursor:pointer; max-width:300px;">
        <div class="footer-nav-icon"><i class="fa-solid fa-arrow-left"></i></div>
        <div>
            <div class="footer-nav-direction" style="font-size:10px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:var(--text3); margin-bottom:4px;">Clase Anterior</div>
            <div class="footer-nav-title" style="font-size:14px; font-weight:600; color:var(--text);">U2·C17 — PCR y la Revolución Genética</div>
        </div>
    </a>
    <div style="text-align:center; font-size:12px; color:var(--text3);">
        <div style="font-family:'Playfair Display',serif; font-size:16px; font-weight:700; color:var(--text);">FILOSOFÍA&CIENCIA</div>
        Unidad 3 · Clase 18
    </div>
    <div class="footer-nav-link disabled" style="opacity:.6;cursor:not-allowed; display:flex; align-items:center; gap:12px; padding:16px 24px; border-radius:16px; border:1px solid var(--border); background:var(--card); max-width:300px; justify-content:flex-end;">
        <div style="text-align:right;">
            <div class="footer-nav-direction" style="font-size:10px; font-weight:700; letter-spacing:0.15em; text-transform:uppercase; color:var(--text3); margin-bottom:4px;">Siguiente Clase</div>
            <div class="footer-nav-title" style="font-size:14px; font-weight:600; color:var(--text);">Próximamente</div>
        </div>
        <div class="footer-nav-icon"><i class="fa-solid fa-arrow-right"></i></div>
    </div>
</nav>

"""

with open('d:/filosofia_experimental/unidad3-clase18.html', 'w', encoding='utf-8') as f:
    f.write(html)
    f.write(scripts_and_close)
