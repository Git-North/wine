1 stdcall GdipAddPathArc(ptr float float float float float float)
2 stdcall GdipAddPathArcI(ptr long long long long float float)
3 stdcall GdipAddPathBezier(ptr float float float float float float float float)
4 stdcall GdipAddPathBezierI(ptr long long long long long long long long)
5 stdcall GdipAddPathBeziers(ptr ptr long)
6 stdcall GdipAddPathBeziersI(ptr ptr long)
7 stdcall GdipAddPathClosedCurve2(ptr ptr long float)
8 stdcall GdipAddPathClosedCurve2I(ptr ptr long float)
9 stdcall GdipAddPathClosedCurve(ptr ptr long)
10 stdcall GdipAddPathClosedCurveI(ptr ptr long)
11 stdcall GdipAddPathCurve2(ptr ptr long float)
12 stdcall GdipAddPathCurve2I(ptr ptr long float)
13 stdcall GdipAddPathCurve3(ptr ptr long long long float)
14 stdcall GdipAddPathCurve3I(ptr ptr long long long float)
15 stdcall GdipAddPathCurve(ptr ptr long)
16 stdcall GdipAddPathCurveI(ptr ptr long)
17 stdcall GdipAddPathEllipse(ptr float float float float)
18 stdcall GdipAddPathEllipseI(ptr long long long long)
19 stdcall GdipAddPathLine2(ptr ptr long)
20 stdcall GdipAddPathLine2I(ptr ptr long)
21 stdcall GdipAddPathLine(ptr float float float float)
22 stdcall GdipAddPathLineI(ptr long long long long)
23 stdcall GdipAddPathPath(ptr ptr long)
24 stdcall GdipAddPathPie(ptr float float float float float float)
25 stdcall GdipAddPathPieI(ptr long long long long float float)
26 stdcall GdipAddPathPolygon(ptr ptr long)
27 stdcall GdipAddPathPolygonI(ptr ptr long)
28 stdcall GdipAddPathRectangle(ptr float float float float)
29 stdcall GdipAddPathRectangleI(ptr long long long long)
30 stdcall GdipAddPathRectangles(ptr ptr long)
31 stdcall GdipAddPathRectanglesI(ptr ptr long)
32 stdcall GdipAddPathString(ptr wstr long ptr long float ptr ptr)
33 stdcall GdipAddPathStringI(ptr wstr long ptr long float ptr ptr)
34 stdcall GdipAlloc(long)
35 stdcall GdipBeginContainer2(ptr ptr)
36 stdcall GdipBeginContainer(ptr ptr ptr long ptr)
37 stdcall GdipBeginContainerI(ptr ptr ptr long ptr)
38 stdcall GdipBitmapGetPixel(ptr long long ptr)
39 stdcall GdipBitmapLockBits(ptr ptr long long ptr)
40 stdcall GdipBitmapSetPixel(ptr long long long)
41 stdcall GdipBitmapSetResolution(ptr float float)
42 stdcall GdipBitmapUnlockBits(ptr ptr)
43 stdcall GdipClearPathMarkers(ptr)
44 stdcall GdipCloneBitmapArea(float float float float long ptr ptr)
45 stdcall GdipCloneBitmapAreaI(long long long long long ptr ptr)
46 stdcall GdipCloneBrush(ptr ptr)
47 stdcall GdipCloneCustomLineCap(ptr ptr)
48 stdcall GdipCloneFont(ptr ptr)
49 stdcall GdipCloneFontFamily(ptr ptr)
50 stdcall GdipCloneImage(ptr ptr)
51 stdcall GdipCloneImageAttributes(ptr ptr)
52 stdcall GdipCloneMatrix(ptr ptr)
53 stdcall GdipClonePath(ptr ptr)
54 stdcall GdipClonePen(ptr ptr)
55 stdcall GdipCloneRegion(ptr ptr)
56 stdcall GdipCloneStringFormat(ptr ptr)
57 stdcall GdipClosePathFigure(ptr)
58 stdcall GdipClosePathFigures(ptr)
59 stdcall GdipCombineRegionPath(ptr ptr long)
60 stdcall GdipCombineRegionRect(ptr ptr long)
61 stdcall GdipCombineRegionRectI(ptr ptr long)
62 stdcall GdipCombineRegionRegion(ptr ptr long)
63 stdcall GdipComment(ptr long ptr)
64 stdcall GdipCreateAdjustableArrowCap(float float long ptr)
65 stub GdipCreateBitmapFromDirectDrawSurface
66 stdcall GdipCreateBitmapFromFile(wstr ptr)
67 stdcall GdipCreateBitmapFromFileICM(wstr ptr)
68 stdcall GdipCreateBitmapFromGdiDib(ptr ptr ptr)
69 stdcall GdipCreateBitmapFromGraphics(long long ptr ptr)
70 stdcall GdipCreateBitmapFromHBITMAP(long long ptr)
71 stdcall GdipCreateBitmapFromHICON(long ptr)
72 stdcall GdipCreateBitmapFromResource(long wstr ptr)
73 stdcall GdipCreateBitmapFromScan0(long long long long ptr ptr)
74 stdcall GdipCreateBitmapFromStream(ptr ptr)
75 stdcall GdipCreateBitmapFromStreamICM(ptr ptr)
76 stdcall GdipCreateCachedBitmap(ptr ptr ptr)
77 stdcall GdipCreateCustomLineCap(ptr ptr long float ptr)
78 stdcall GdipCreateFont(ptr float long long ptr)
79 stdcall GdipCreateFontFamilyFromName(wstr ptr ptr)
80 stdcall GdipCreateFontFromDC(long ptr)
81 stdcall GdipCreateFontFromLogfontA(long ptr ptr)
82 stdcall GdipCreateFontFromLogfontW(long ptr ptr)
83 stdcall GdipCreateFromHDC2(long long ptr)
84 stdcall GdipCreateFromHDC(long ptr)
85 stdcall GdipCreateFromHWND(long ptr)
86 stdcall GdipCreateFromHWNDICM(long ptr)
87 stdcall GdipCreateHBITMAPFromBitmap(ptr ptr long)
88 stdcall GdipCreateHICONFromBitmap(ptr ptr)
89 stdcall GdipCreateHalftonePalette()
90 stdcall GdipCreateHatchBrush(long long long ptr)
91 stdcall GdipCreateImageAttributes(ptr)
92 stdcall GdipCreateLineBrush(ptr ptr long long long ptr)
93 stdcall GdipCreateLineBrushFromRect(ptr long long long long ptr)
94 stdcall GdipCreateLineBrushFromRectI(ptr long long long long ptr)
95 stdcall GdipCreateLineBrushFromRectWithAngle(ptr long long float long long ptr)
96 stdcall GdipCreateLineBrushFromRectWithAngleI(ptr long long float long long ptr)
97 stdcall GdipCreateLineBrushI(ptr ptr long long long ptr)
98 stdcall GdipCreateMatrix2(float float float float float float ptr)
99 stdcall GdipCreateMatrix3(ptr ptr ptr)
100 stdcall GdipCreateMatrix3I(ptr ptr ptr)
101 stdcall GdipCreateMatrix(ptr)
102 stdcall GdipCreateMetafileFromEmf(ptr long ptr)
103 stdcall GdipCreateMetafileFromFile(wstr ptr)
104 stdcall GdipCreateMetafileFromStream(ptr ptr)
105 stdcall GdipCreateMetafileFromWmf(ptr long ptr ptr)
106 stdcall GdipCreateMetafileFromWmfFile(wstr ptr ptr)
107 stdcall GdipCreatePath2(ptr ptr long long ptr)
108 stdcall GdipCreatePath2I(ptr ptr long long ptr)
109 stdcall GdipCreatePath(long ptr)
110 stdcall GdipCreatePathGradient(ptr long long ptr)
111 stdcall GdipCreatePathGradientFromPath(ptr ptr)
112 stdcall GdipCreatePathGradientI(ptr long long ptr)
113 stdcall GdipCreatePathIter(ptr ptr)
114 stdcall GdipCreatePen1(long float long ptr)
115 stdcall GdipCreatePen2(ptr float long ptr)
116 stdcall GdipCreateRegion(ptr)
117 stdcall GdipCreateRegionHrgn(ptr ptr)
118 stdcall GdipCreateRegionPath(ptr ptr)
119 stdcall GdipCreateRegionRect(ptr ptr)
120 stdcall GdipCreateRegionRectI(ptr ptr)
121 stdcall GdipCreateRegionRgnData(ptr long ptr)
122 stdcall GdipCreateSolidFill(long ptr)
123 stdcall GdipCreateStreamOnFile(wstr long ptr)
124 stdcall GdipCreateStringFormat(long long ptr)
125 stdcall GdipCreateTexture2(ptr long float float float float ptr)
126 stdcall GdipCreateTexture2I(ptr long long long long long ptr)
127 stdcall GdipCreateTexture(ptr long ptr)
128 stdcall GdipCreateTextureIA(ptr ptr float float float float ptr)
129 stdcall GdipCreateTextureIAI(ptr ptr long long long long ptr)
130 stdcall GdipDeleteBrush(ptr)
131 stdcall GdipDeleteCachedBitmap(ptr)
132 stdcall GdipDeleteCustomLineCap(ptr)
133 stdcall GdipDeleteFont(ptr)
134 stdcall GdipDeleteFontFamily(ptr)
135 stdcall GdipDeleteGraphics(ptr)
136 stdcall GdipDeleteMatrix(ptr)
137 stdcall GdipDeletePath(ptr)
138 stdcall GdipDeletePathIter(ptr)
139 stdcall GdipDeletePen(ptr)
140 stdcall GdipDeletePrivateFontCollection(ptr)
141 stdcall GdipDeleteRegion(ptr)
142 stdcall GdipDeleteStringFormat(ptr)
143 stdcall GdipDisposeImage(ptr)
144 stdcall GdipDisposeImageAttributes(ptr)
145 stdcall GdipDrawArc(ptr ptr float float float float float float)
146 stdcall GdipDrawArcI(ptr ptr long long long long float float)
147 stdcall GdipDrawBezier(ptr ptr float float float float float float float float)
148 stdcall GdipDrawBezierI(ptr ptr long long long long long long long long)
149 stdcall GdipDrawBeziers(ptr ptr ptr long)
150 stdcall GdipDrawBeziersI(ptr ptr ptr long)
151 stdcall GdipDrawCachedBitmap(ptr ptr long long)
152 stdcall GdipDrawClosedCurve2(ptr ptr ptr long float)
153 stdcall GdipDrawClosedCurve2I(ptr ptr ptr long float)
154 stdcall GdipDrawClosedCurve(ptr ptr ptr long)
155 stdcall GdipDrawClosedCurveI(ptr ptr ptr long)
156 stdcall GdipDrawCurve2(ptr ptr ptr long float)
157 stdcall GdipDrawCurve2I(ptr ptr ptr long float)
158 stdcall GdipDrawCurve3(ptr ptr ptr long long long float)
159 stdcall GdipDrawCurve3I(ptr ptr ptr long long long float)
160 stdcall GdipDrawCurve(ptr ptr ptr long)
161 stdcall GdipDrawCurveI(ptr ptr ptr long)
162 stdcall GdipDrawDriverString(ptr ptr long ptr ptr ptr long ptr)
163 stdcall GdipDrawEllipse(ptr ptr float float float float)
164 stdcall GdipDrawEllipseI(ptr ptr long long long long)
165 stdcall GdipDrawImage(ptr ptr float float)
166 stdcall GdipDrawImageI(ptr ptr long long)
167 stdcall GdipDrawImagePointRect(ptr ptr float float float float float float long)
168 stdcall GdipDrawImagePointRectI(ptr ptr long long long long long long long)
169 stdcall GdipDrawImagePoints(ptr ptr ptr long)
170 stdcall GdipDrawImagePointsI(ptr ptr ptr long)
171 stdcall GdipDrawImagePointsRect(ptr ptr ptr long float float float float long ptr ptr ptr)
172 stdcall GdipDrawImagePointsRectI(ptr ptr ptr long long long long long long ptr ptr ptr)
173 stdcall GdipDrawImageRect(ptr ptr float float float float)
174 stdcall GdipDrawImageRectI(ptr ptr long long long long)
175 stdcall GdipDrawImageRectRect(ptr ptr float float float float float float float float long ptr ptr ptr)
176 stdcall GdipDrawImageRectRectI(ptr ptr long long long long long long long long long ptr ptr ptr)
177 stdcall GdipDrawLine(ptr ptr float float float float)
178 stdcall GdipDrawLineI(ptr ptr long long long long)
179 stdcall GdipDrawLines(ptr ptr ptr long)
180 stdcall GdipDrawLinesI(ptr ptr ptr long)
181 stdcall GdipDrawPath(ptr ptr ptr)
182 stdcall GdipDrawPie(ptr ptr float float float float float float)
183 stdcall GdipDrawPieI(ptr ptr long long long long float float)
184 stdcall GdipDrawPolygon(ptr ptr ptr long)
185 stdcall GdipDrawPolygonI(ptr ptr ptr long)
186 stdcall GdipDrawRectangle(ptr ptr float float float float)
187 stdcall GdipDrawRectangleI(ptr ptr long long long long)
188 stdcall GdipDrawRectangles(ptr ptr ptr long)
189 stdcall GdipDrawRectanglesI(ptr ptr ptr long)
190 stdcall GdipDrawString(ptr wstr long ptr ptr ptr ptr)
191 stdcall GdipEmfToWmfBits(ptr long ptr long long)
192 stdcall GdipEndContainer(ptr long)
193 stdcall GdipEnumerateMetafileDestPoint(ptr ptr ptr ptr ptr ptr)
194 stdcall GdipEnumerateMetafileDestPointI(ptr ptr ptr ptr ptr ptr)
195 stub GdipEnumerateMetafileDestPoints
196 stub GdipEnumerateMetafileDestPointsI
197 stdcall GdipEnumerateMetafileDestRect(ptr ptr ptr ptr ptr ptr)
198 stdcall GdipEnumerateMetafileDestRectI(ptr ptr ptr ptr ptr ptr)
199 stub GdipEnumerateMetafileSrcRectDestPoint
200 stub GdipEnumerateMetafileSrcRectDestPointI
201 stdcall GdipEnumerateMetafileSrcRectDestPoints(ptr ptr ptr long ptr long ptr ptr ptr)
202 stub GdipEnumerateMetafileSrcRectDestPointsI
203 stdcall GdipEnumerateMetafileSrcRectDestRect(ptr ptr ptr ptr long ptr ptr ptr)
204 stdcall GdipEnumerateMetafileSrcRectDestRectI(ptr ptr ptr ptr long ptr ptr ptr)
205 stdcall GdipFillClosedCurve2(ptr ptr ptr long float long)
206 stdcall GdipFillClosedCurve2I(ptr ptr ptr long float long)
207 stdcall GdipFillClosedCurve(ptr ptr ptr long)
208 stdcall GdipFillClosedCurveI(ptr ptr ptr long)
209 stdcall GdipFillEllipse(ptr ptr float float float float)
210 stdcall GdipFillEllipseI(ptr ptr long long long long)
211 stdcall GdipFillPath(ptr ptr ptr)
212 stdcall GdipFillPie(ptr ptr float float float float float float)
213 stdcall GdipFillPieI(ptr ptr long long long long float float)
214 stdcall GdipFillPolygon2(ptr ptr ptr long)
215 stdcall GdipFillPolygon2I(ptr ptr ptr long)
216 stdcall GdipFillPolygon(ptr ptr ptr long long)
217 stdcall GdipFillPolygonI(ptr ptr ptr long long)
218 stdcall GdipFillRectangle(ptr ptr float float float float)
219 stdcall GdipFillRectangleI(ptr ptr long long long long)
220 stdcall GdipFillRectangles(ptr ptr ptr long)
221 stdcall GdipFillRectanglesI(ptr ptr ptr long)
222 stdcall GdipFillRegion(ptr ptr ptr)
223 stdcall GdipFlattenPath(ptr ptr float)
224 stdcall GdipFlush(ptr long)
225 stdcall GdipFree(ptr)
226 stdcall GdipGetAdjustableArrowCapFillState(ptr ptr)
227 stdcall GdipGetAdjustableArrowCapHeight(ptr ptr)
228 stdcall GdipGetAdjustableArrowCapMiddleInset(ptr ptr)
229 stdcall GdipGetAdjustableArrowCapWidth(ptr ptr)
230 stdcall GdipGetAllPropertyItems(ptr long long ptr)
231 stdcall GdipGetBrushType(ptr ptr)
232 stdcall GdipGetCellAscent(ptr long ptr)
233 stdcall GdipGetCellDescent(ptr long ptr)
234 stdcall GdipGetClip(ptr ptr)
235 stdcall GdipGetClipBounds(ptr ptr)
236 stdcall GdipGetClipBoundsI(ptr ptr)
237 stdcall GdipGetCompositingMode(ptr ptr)
238 stdcall GdipGetCompositingQuality(ptr ptr)
239 stdcall GdipGetCustomLineCapBaseCap(ptr ptr)
240 stdcall GdipGetCustomLineCapBaseInset(ptr ptr)
241 stub GdipGetCustomLineCapStrokeCaps
242 stdcall GdipGetCustomLineCapStrokeJoin(ptr ptr)
243 stdcall GdipGetCustomLineCapType(ptr ptr)
244 stdcall GdipGetCustomLineCapWidthScale(ptr ptr)
245 stdcall GdipGetDC(ptr ptr)
246 stdcall GdipGetDpiX(ptr ptr)
247 stdcall GdipGetDpiY(ptr ptr)
248 stdcall GdipGetEmHeight(ptr long ptr)
249 stub GdipGetEncoderParameterList
250 stdcall GdipGetEncoderParameterListSize(ptr ptr ptr)
251 stdcall GdipGetFamily(ptr ptr)
252 stdcall GdipGetFamilyName(ptr ptr long)
253 stdcall GdipGetFontCollectionFamilyCount(ptr ptr)
254 stdcall GdipGetFontCollectionFamilyList(ptr long ptr ptr)
255 stdcall GdipGetFontHeight(ptr ptr ptr)
256 stdcall GdipGetFontHeightGivenDPI(ptr float ptr)
257 stdcall GdipGetFontSize(ptr ptr)
258 stdcall GdipGetFontStyle(ptr ptr)
259 stdcall GdipGetFontUnit(ptr ptr)
260 stdcall GdipGetGenericFontFamilyMonospace(ptr)
261 stdcall GdipGetGenericFontFamilySansSerif(ptr)
262 stdcall GdipGetGenericFontFamilySerif(ptr)
263 stdcall GdipGetHatchBackgroundColor(ptr ptr)
264 stdcall GdipGetHatchForegroundColor(ptr ptr)
265 stdcall GdipGetHatchStyle(ptr ptr)
266 stdcall GdipGetHemfFromMetafile(ptr ptr)
267 stdcall GdipGetImageAttributesAdjustedPalette(ptr ptr long)
268 stdcall GdipGetImageBounds(ptr ptr ptr)
269 stdcall GdipGetImageDecoders(long long ptr)
270 stdcall GdipGetImageDecodersSize(ptr ptr)
271 stdcall GdipGetImageDimension(ptr ptr ptr)
272 stdcall GdipGetImageEncoders(long long ptr)
273 stdcall GdipGetImageEncodersSize(ptr ptr)
274 stdcall GdipGetImageFlags(ptr ptr)
275 stdcall GdipGetImageGraphicsContext(ptr ptr)
276 stdcall GdipGetImageHeight(ptr ptr)
277 stdcall GdipGetImageHorizontalResolution(ptr ptr)
278 stdcall GdipGetImagePalette(ptr ptr long)
279 stdcall GdipGetImagePaletteSize(ptr ptr)
280 stdcall GdipGetImagePixelFormat(ptr ptr)
281 stdcall GdipGetImageRawFormat(ptr ptr)
282 stdcall GdipGetImageThumbnail(ptr long long ptr ptr ptr)
283 stdcall GdipGetImageType(ptr ptr)
284 stdcall GdipGetImageVerticalResolution(ptr ptr)
285 stdcall GdipGetImageWidth(ptr ptr)
286 stdcall GdipGetInterpolationMode(ptr ptr)
287 stdcall GdipGetLineBlend(ptr ptr ptr long)
288 stdcall GdipGetLineBlendCount(ptr ptr)
289 stdcall GdipGetLineColors(ptr ptr)
290 stdcall GdipGetLineGammaCorrection(ptr ptr)
291 stdcall GdipGetLinePresetBlend(ptr ptr ptr long)
292 stdcall GdipGetLinePresetBlendCount(ptr ptr)
293 stdcall GdipGetLineRect(ptr ptr)
294 stdcall GdipGetLineRectI(ptr ptr)
295 stdcall GdipGetLineSpacing(ptr long ptr)
296 stdcall GdipGetLineTransform(ptr ptr)
297 stdcall GdipGetLineWrapMode(ptr ptr)
298 stdcall GdipGetLogFontA(ptr ptr ptr)
299 stdcall GdipGetLogFontW(ptr ptr ptr)
300 stdcall GdipGetMatrixElements(ptr ptr)
301 stdcall GdipGetMetafileDownLevelRasterizationLimit(ptr ptr)
302 stdcall GdipGetMetafileHeaderFromEmf(ptr ptr)
303 stdcall GdipGetMetafileHeaderFromFile(wstr ptr)
304 stdcall GdipGetMetafileHeaderFromMetafile(ptr ptr)
305 stdcall GdipGetMetafileHeaderFromStream(ptr ptr)
306 stdcall GdipGetMetafileHeaderFromWmf(ptr ptr ptr)
307 stdcall GdipGetNearestColor(ptr ptr)
308 stdcall GdipGetPageScale(ptr ptr)
309 stdcall GdipGetPageUnit(ptr ptr)
310 stdcall GdipGetPathData(ptr ptr)
311 stdcall GdipGetPathFillMode(ptr ptr)
312 stdcall GdipGetPathGradientBlend(ptr ptr ptr long)
313 stdcall GdipGetPathGradientBlendCount(ptr ptr)
314 stdcall GdipGetPathGradientCenterColor(ptr ptr)
315 stdcall GdipGetPathGradientCenterPoint(ptr ptr)
316 stdcall GdipGetPathGradientCenterPointI(ptr ptr)
317 stdcall GdipGetPathGradientFocusScales(ptr ptr ptr)
318 stdcall GdipGetPathGradientGammaCorrection(ptr ptr)
319 stdcall GdipGetPathGradientPath(ptr ptr)
320 stdcall GdipGetPathGradientPointCount(ptr ptr)
321 stdcall GdipGetPathGradientPresetBlend(ptr ptr ptr long)
322 stdcall GdipGetPathGradientPresetBlendCount(ptr ptr)
323 stdcall GdipGetPathGradientRect(ptr ptr)
324 stdcall GdipGetPathGradientRectI(ptr ptr)
325 stdcall GdipGetPathGradientSurroundColorCount(ptr ptr)
326 stdcall GdipGetPathGradientSurroundColorsWithCount(ptr ptr ptr)
327 stdcall GdipGetPathGradientTransform(ptr ptr)
328 stdcall GdipGetPathGradientWrapMode(ptr ptr)
329 stdcall GdipGetPathLastPoint(ptr ptr)
330 stdcall GdipGetPathPoints(ptr ptr long)
331 stdcall GdipGetPathPointsI(ptr ptr long)
332 stdcall GdipGetPathTypes(ptr ptr long)
333 stdcall GdipGetPathWorldBounds(ptr ptr ptr ptr)
334 stdcall GdipGetPathWorldBoundsI(ptr ptr ptr ptr)
335 stdcall GdipGetPenBrushFill(ptr ptr)
336 stdcall GdipGetPenColor(ptr ptr)
337 stdcall GdipGetPenCompoundArray(ptr ptr long)
338 stdcall GdipGetPenCompoundCount(ptr ptr)
339 stdcall GdipGetPenCustomEndCap(ptr ptr)
340 stdcall GdipGetPenCustomStartCap(ptr ptr)
341 stdcall GdipGetPenDashArray(ptr ptr long)
342 stdcall GdipGetPenDashCap197819(ptr ptr)
343 stdcall GdipGetPenDashCount(ptr ptr)
344 stdcall GdipGetPenDashOffset(ptr ptr)
345 stdcall GdipGetPenDashStyle(ptr ptr)
346 stdcall GdipGetPenEndCap(ptr ptr)
347 stdcall GdipGetPenFillType(ptr ptr)
348 stdcall GdipGetPenLineJoin(ptr ptr)
349 stdcall GdipGetPenMiterLimit(ptr ptr)
350 stdcall GdipGetPenMode(ptr ptr)
351 stdcall GdipGetPenStartCap(ptr ptr)
352 stdcall GdipGetPenTransform(ptr ptr)
353 stdcall GdipGetPenUnit(ptr ptr)
354 stdcall GdipGetPenWidth(ptr ptr)
355 stdcall GdipGetPixelOffsetMode(ptr ptr)
356 stdcall GdipGetPointCount(ptr ptr)
357 stdcall GdipGetPropertyCount(ptr ptr)
358 stdcall GdipGetPropertyIdList(ptr long ptr)
359 stdcall GdipGetPropertyItem(ptr long long ptr)
360 stdcall GdipGetPropertyItemSize(ptr long ptr)
361 stdcall GdipGetPropertySize(ptr ptr ptr)
362 stdcall GdipGetRegionBounds(ptr ptr ptr)
363 stdcall GdipGetRegionBoundsI(ptr ptr ptr)
364 stdcall GdipGetRegionData(ptr ptr long ptr)
365 stdcall GdipGetRegionDataSize(ptr ptr)
366 stdcall GdipGetRegionHRgn(ptr ptr ptr)
367 stdcall GdipGetRegionScans(ptr ptr ptr ptr)
368 stdcall GdipGetRegionScansCount(ptr ptr ptr)
369 stdcall GdipGetRegionScansI(ptr ptr ptr ptr)
370 stdcall GdipGetRenderingOrigin(ptr ptr ptr)
371 stdcall GdipGetSmoothingMode(ptr ptr)
372 stdcall GdipGetSolidFillColor(ptr ptr)
373 stdcall GdipGetStringFormatAlign(ptr ptr)
374 stdcall GdipGetStringFormatDigitSubstitution(ptr ptr ptr)
375 stdcall GdipGetStringFormatFlags(ptr ptr)
376 stdcall GdipGetStringFormatHotkeyPrefix(ptr ptr)
377 stdcall GdipGetStringFormatLineAlign(ptr ptr)
378 stdcall GdipGetStringFormatMeasurableCharacterRangeCount(ptr ptr)
379 stdcall GdipGetStringFormatTabStopCount(ptr ptr)
380 stdcall GdipGetStringFormatTabStops(ptr long ptr ptr)
381 stdcall GdipGetStringFormatTrimming(ptr ptr)
382 stdcall GdipGetTextContrast(ptr ptr)
383 stdcall GdipGetTextRenderingHint(ptr ptr)
384 stdcall GdipGetTextureImage(ptr ptr)
385 stdcall GdipGetTextureTransform(ptr ptr)
386 stdcall GdipGetTextureWrapMode(ptr ptr)
387 stdcall GdipGetVisibleClipBounds(ptr ptr)
388 stdcall GdipGetVisibleClipBoundsI(ptr ptr)
389 stdcall GdipGetWorldTransform(ptr ptr)
390 stdcall GdipGraphicsClear(ptr long)
391 stdcall GdipImageForceValidation(ptr)
392 stdcall GdipImageGetFrameCount(ptr ptr ptr)
393 stdcall GdipImageGetFrameDimensionsCount(ptr ptr)
394 stdcall GdipImageGetFrameDimensionsList(ptr ptr long)
395 stdcall GdipImageRotateFlip(ptr long)
396 stdcall GdipImageSelectActiveFrame(ptr ptr long)
397 stdcall GdipInvertMatrix(ptr)
398 stdcall GdipIsClipEmpty(ptr ptr)
399 stdcall GdipIsEmptyRegion(ptr ptr ptr)
400 stdcall GdipIsEqualRegion(ptr ptr ptr ptr)
401 stdcall GdipIsInfiniteRegion(ptr ptr ptr)
402 stdcall GdipIsMatrixEqual(ptr ptr ptr)
403 stdcall GdipIsMatrixIdentity(ptr ptr)
404 stdcall GdipIsMatrixInvertible(ptr ptr)
405 stdcall GdipIsOutlineVisiblePathPoint(ptr float float ptr ptr ptr)
406 stdcall GdipIsOutlineVisiblePathPointI(ptr long long ptr ptr ptr)
407 stdcall GdipIsStyleAvailable(ptr long ptr)
408 stdcall GdipIsVisibleClipEmpty(ptr ptr)
409 stdcall GdipIsVisiblePathPoint(ptr float float ptr ptr)
410 stdcall GdipIsVisiblePathPointI(ptr long long ptr ptr)
411 stdcall GdipIsVisiblePoint(ptr float float ptr)
412 stdcall GdipIsVisiblePointI(ptr long long ptr)
413 stdcall GdipIsVisibleRect(ptr float float float float ptr)
414 stdcall GdipIsVisibleRectI(ptr long long long long ptr)
415 stdcall GdipIsVisibleRegionPoint(ptr float float ptr ptr)
416 stdcall GdipIsVisibleRegionPointI(ptr long long ptr ptr)
417 stdcall GdipIsVisibleRegionRect(ptr float float float float ptr ptr)
418 stdcall GdipIsVisibleRegionRectI(ptr long long long long ptr ptr)
419 stdcall GdipLoadImageFromFile(wstr ptr)
420 stdcall GdipLoadImageFromFileICM(wstr ptr)
421 stdcall GdipLoadImageFromStream(ptr ptr)
422 stdcall GdipLoadImageFromStreamICM(ptr ptr)
423 stdcall GdipMeasureCharacterRanges(ptr wstr long ptr ptr ptr long ptr)
424 stdcall GdipMeasureDriverString(ptr ptr long ptr ptr long ptr ptr)
425 stdcall GdipMeasureString(ptr wstr long ptr ptr ptr ptr ptr ptr)
426 stdcall GdipMultiplyLineTransform(ptr ptr long)
427 stdcall GdipMultiplyMatrix(ptr ptr long)
428 stdcall GdipMultiplyPathGradientTransform(ptr ptr long)
429 stdcall GdipMultiplyPenTransform(ptr ptr long)
430 stdcall GdipMultiplyTextureTransform(ptr ptr long)
431 stdcall GdipMultiplyWorldTransform(ptr ptr long)
432 stdcall GdipNewInstalledFontCollection(ptr)
433 stdcall GdipNewPrivateFontCollection(ptr)
434 stdcall GdipPathIterCopyData(ptr ptr ptr ptr long long)
435 stdcall GdipPathIterEnumerate(ptr ptr ptr ptr long)
436 stdcall GdipPathIterGetCount(ptr ptr)
437 stdcall GdipPathIterGetSubpathCount(ptr ptr)
438 stdcall GdipPathIterHasCurve(ptr ptr)
439 stdcall GdipPathIterIsValid(ptr ptr)
440 stdcall GdipPathIterNextMarker(ptr ptr ptr ptr)
441 stdcall GdipPathIterNextMarkerPath(ptr ptr ptr)
442 stdcall GdipPathIterNextPathType(ptr ptr ptr ptr ptr)
443 stdcall GdipPathIterNextSubpath(ptr ptr ptr ptr ptr)
444 stdcall GdipPathIterNextSubpathPath(ptr ptr ptr ptr)
445 stdcall GdipPathIterRewind(ptr)
446 stdcall GdipPlayMetafileRecord(ptr long long long ptr)
447 stdcall GdipPrivateAddFontFile(ptr wstr)
448 stdcall GdipPrivateAddMemoryFont(ptr ptr long)
449 stdcall GdipRecordMetafile(long long ptr long wstr ptr)
450 stdcall GdipRecordMetafileFileName(wstr long long ptr long wstr ptr)
451 stdcall GdipRecordMetafileFileNameI(wstr long long ptr long wstr ptr)
452 stdcall GdipRecordMetafileI(long long ptr long wstr ptr)
453 stdcall GdipRecordMetafileStream(ptr long long ptr long wstr ptr)
454 stdcall GdipRecordMetafileStreamI(ptr long long ptr long wstr ptr)
455 stdcall GdipReleaseDC(ptr ptr)
456 stdcall GdipRemovePropertyItem(ptr long)
457 stdcall GdipResetClip(ptr)
458 stdcall GdipResetImageAttributes(ptr long)
459 stdcall GdipResetLineTransform(ptr)
460 stdcall GdipResetPageTransform(ptr)
461 stdcall GdipResetPath(ptr)
462 stdcall GdipResetPathGradientTransform(ptr)
463 stdcall GdipResetPenTransform(ptr)
464 stdcall GdipResetTextureTransform(ptr)
465 stdcall GdipResetWorldTransform(ptr)
466 stdcall GdipRestoreGraphics(ptr long)
467 stdcall GdipReversePath(ptr)
468 stdcall GdipRotateLineTransform(ptr float long)
469 stdcall GdipRotateMatrix(ptr float long)
470 stdcall GdipRotatePathGradientTransform(ptr float long)
471 stdcall GdipRotatePenTransform(ptr float long)
472 stdcall GdipRotateTextureTransform(ptr float long)
473 stdcall GdipRotateWorldTransform(ptr float long)
474 stdcall GdipSaveAdd(ptr ptr)
475 stdcall GdipSaveAddImage(ptr ptr ptr)
476 stdcall GdipSaveGraphics(ptr ptr)
477 stdcall GdipSaveImageToFile(ptr wstr ptr ptr)
478 stdcall GdipSaveImageToStream(ptr ptr ptr ptr)
479 stdcall GdipScaleLineTransform(ptr float float long)
480 stdcall GdipScaleMatrix(ptr float float long)
481 stdcall GdipScalePathGradientTransform(ptr float float long)
482 stdcall GdipScalePenTransform(ptr float float long)
483 stdcall GdipScaleTextureTransform(ptr float float long)
484 stdcall GdipScaleWorldTransform(ptr float float long)
485 stdcall GdipSetAdjustableArrowCapFillState(ptr long)
486 stdcall GdipSetAdjustableArrowCapHeight(ptr float)
487 stdcall GdipSetAdjustableArrowCapMiddleInset(ptr float)
488 stdcall GdipSetAdjustableArrowCapWidth(ptr float)
489 stdcall GdipSetClipGraphics(ptr ptr long)
490 stdcall GdipSetClipHrgn(ptr long long)
491 stdcall GdipSetClipPath(ptr ptr long)
492 stdcall GdipSetClipRect(ptr float float float float long)
493 stdcall GdipSetClipRectI(ptr long long long long long)
494 stdcall GdipSetClipRegion(ptr ptr long)
495 stdcall GdipSetCompositingMode(ptr long)
496 stdcall GdipSetCompositingQuality(ptr long)
497 stdcall GdipSetCustomLineCapBaseCap(ptr long)
498 stdcall GdipSetCustomLineCapBaseInset(ptr float)
499 stdcall GdipSetCustomLineCapStrokeCaps(ptr long long)
500 stdcall GdipSetCustomLineCapStrokeJoin(ptr long)
501 stdcall GdipSetCustomLineCapWidthScale(ptr float)
502 stdcall GdipSetEmpty(ptr)
503 stdcall GdipSetImageAttributesCachedBackground(ptr long)
504 stdcall GdipSetImageAttributesColorKeys(ptr long long long long)
505 stdcall GdipSetImageAttributesColorMatrix(ptr long long ptr ptr long)
506 stdcall GdipSetImageAttributesGamma(ptr long long float)
507 stdcall GdipSetImageAttributesNoOp(ptr long long)
508 stdcall GdipSetImageAttributesOutputChannel(ptr long long long)
509 stdcall GdipSetImageAttributesOutputChannelColorProfile(ptr long long wstr)
510 stdcall GdipSetImageAttributesRemapTable(ptr long long long ptr)
511 stdcall GdipSetImageAttributesThreshold(ptr long long float)
512 stdcall GdipSetImageAttributesToIdentity(ptr long)
513 stdcall GdipSetImageAttributesWrapMode(ptr long long long)
514 stdcall GdipSetImagePalette(ptr ptr)
515 stdcall GdipSetInfinite(ptr)
516 stdcall GdipSetInterpolationMode(ptr long)
517 stdcall GdipSetLineBlend(ptr ptr ptr long)
518 stdcall GdipSetLineColors(ptr long long)
519 stdcall GdipSetLineGammaCorrection(ptr long)
520 stdcall GdipSetLineLinearBlend(ptr float float)
521 stdcall GdipSetLinePresetBlend(ptr ptr ptr long)
522 stdcall GdipSetLineSigmaBlend(ptr float float)
523 stdcall GdipSetLineTransform(ptr ptr)
524 stdcall GdipSetLineWrapMode(ptr long)
525 stdcall GdipSetMatrixElements(ptr float float float float float float)
526 stdcall GdipSetMetafileDownLevelRasterizationLimit(ptr long)
527 stdcall GdipSetPageScale(ptr float)
528 stdcall GdipSetPageUnit(ptr long)
529 stdcall GdipSetPathFillMode(ptr long)
530 stdcall GdipSetPathGradientBlend(ptr ptr ptr long)
531 stdcall GdipSetPathGradientCenterColor(ptr long)
532 stdcall GdipSetPathGradientCenterPoint(ptr ptr)
533 stdcall GdipSetPathGradientCenterPointI(ptr ptr)
534 stdcall GdipSetPathGradientFocusScales(ptr float float)
535 stdcall GdipSetPathGradientGammaCorrection(ptr long)
536 stdcall GdipSetPathGradientLinearBlend(ptr float float)
537 stdcall GdipSetPathGradientPath(ptr ptr)
538 stdcall GdipSetPathGradientPresetBlend(ptr ptr ptr long)
539 stdcall GdipSetPathGradientSigmaBlend(ptr float float)
540 stdcall GdipSetPathGradientSurroundColorsWithCount(ptr ptr ptr)
541 stdcall GdipSetPathGradientTransform(ptr ptr)
542 stdcall GdipSetPathGradientWrapMode(ptr long)
543 stdcall GdipSetPathMarker(ptr)
544 stdcall GdipSetPenBrushFill(ptr ptr)
545 stdcall GdipSetPenColor(ptr long)
546 stdcall GdipSetPenCompoundArray(ptr ptr long)
547 stdcall GdipSetPenCustomEndCap(ptr ptr)
548 stdcall GdipSetPenCustomStartCap(ptr ptr)
549 stdcall GdipSetPenDashArray(ptr ptr long)
550 stdcall GdipSetPenDashCap197819(ptr long)
551 stdcall GdipSetPenDashOffset(ptr float)
552 stdcall GdipSetPenDashStyle(ptr long)
553 stdcall GdipSetPenEndCap(ptr long)
554 stdcall GdipSetPenLineCap197819(ptr long long long)
555 stdcall GdipSetPenLineJoin(ptr long)
556 stdcall GdipSetPenMiterLimit(ptr float)
557 stdcall GdipSetPenMode(ptr long)
558 stdcall GdipSetPenStartCap(ptr long)
559 stdcall GdipSetPenTransform(ptr ptr)
560 stub GdipSetPenUnit
561 stdcall GdipSetPenWidth(ptr float)
562 stdcall GdipSetPixelOffsetMode(ptr long)
563 stdcall GdipSetPropertyItem(ptr ptr)
564 stdcall GdipSetRenderingOrigin(ptr long long)
565 stdcall GdipSetSmoothingMode(ptr long)
566 stdcall GdipSetSolidFillColor(ptr long)
567 stdcall GdipSetStringFormatAlign(ptr long)
568 stdcall GdipSetStringFormatDigitSubstitution(ptr long long)
569 stdcall GdipSetStringFormatFlags(ptr long)
570 stdcall GdipSetStringFormatHotkeyPrefix(ptr long)
571 stdcall GdipSetStringFormatLineAlign(ptr long)
572 stdcall GdipSetStringFormatMeasurableCharacterRanges(ptr long ptr)
573 stdcall GdipSetStringFormatTabStops(ptr float long ptr)
574 stdcall GdipSetStringFormatTrimming(ptr long)
575 stdcall GdipSetTextContrast(ptr long)
576 stdcall GdipSetTextRenderingHint(ptr long)
577 stdcall GdipSetTextureTransform(ptr ptr)
578 stdcall GdipSetTextureWrapMode(ptr long)
579 stdcall GdipSetWorldTransform(ptr ptr)
580 stdcall GdipShearMatrix(ptr float float long)
581 stdcall GdipStartPathFigure(ptr)
582 stdcall GdipStringFormatGetGenericDefault(ptr)
583 stdcall GdipStringFormatGetGenericTypographic(ptr)
584 stdcall GdipTestControl(long ptr)
585 stdcall GdipTransformMatrixPoints(ptr ptr long)
586 stdcall GdipTransformMatrixPointsI(ptr ptr long)
587 stdcall GdipTransformPath(ptr ptr)
588 stdcall GdipTransformPoints(ptr long long ptr long)
589 stdcall GdipTransformPointsI(ptr long long ptr long)
590 stdcall GdipTransformRegion(ptr ptr)
591 stdcall GdipTranslateClip(ptr float float)
592 stdcall GdipTranslateClipI(ptr long long)
593 stdcall GdipTranslateLineTransform(ptr float float long)
594 stdcall GdipTranslateMatrix(ptr float float long)
595 stdcall GdipTranslatePathGradientTransform(ptr float float long)
596 stdcall GdipTranslatePenTransform(ptr float float long)
597 stdcall GdipTranslateRegion(ptr float float)
598 stdcall GdipTranslateRegionI(ptr long long)
599 stdcall GdipTranslateTextureTransform(ptr float float long)
600 stdcall GdipTranslateWorldTransform(ptr float float long)
601 stdcall GdipVectorTransformMatrixPoints(ptr ptr long)
602 stdcall GdipVectorTransformMatrixPointsI(ptr ptr long)
603 stdcall GdipWarpPath(ptr ptr ptr long float float float float long float)
604 stdcall GdipWidenPath(ptr ptr ptr float)
605 stdcall GdipWindingModeOutline(ptr ptr float)
606 stdcall GdiplusNotificationHook(ptr)
607 stdcall GdiplusNotificationUnhook(long)
608 stdcall GdiplusShutdown(long) GdiplusShutdown_wrapper
609 stdcall GdiplusStartup(ptr ptr ptr)
610 stdcall GdipFindFirstImageItem(ptr ptr)
611 stub GdipFindNextImageItem
612 stdcall GdipGetImageItemData(ptr ptr)
613 stdcall GdipCreateEffect(int128 ptr)
614 stdcall GdipDeleteEffect(ptr)
615 stdcall GdipGetEffectParameterSize(ptr ptr)
616 stdcall GdipGetEffectParameters(ptr ptr ptr)
617 stdcall GdipSetEffectParameters(ptr ptr long)
618 stdcall GdipInitializePalette(ptr long long long ptr)
619 stdcall GdipBitmapCreateApplyEffect(ptr long ptr ptr ptr ptr long ptr ptr)
620 stdcall GdipBitmapApplyEffect(ptr ptr ptr long ptr ptr)
621 stdcall GdipBitmapGetHistogram(ptr long long ptr ptr ptr ptr)
622 stdcall GdipBitmapGetHistogramSize(long ptr)
623 stdcall GdipBitmapConvertFormat(ptr long long long ptr float)
624 stdcall GdipImageSetAbort(ptr ptr)
625 stdcall GdipGraphicsSetAbort(ptr ptr)
626 stdcall GdipDrawImageFX(ptr ptr ptr ptr ptr ptr long)
627 stdcall GdipConvertToEmfPlus(ptr ptr ptr long wstr ptr)
628 stdcall GdipConvertToEmfPlusToFile(ptr ptr ptr wstr long wstr ptr)
629 stub GdipConvertToEmfPlusToStream
630 stub GdipPlayTSClientRecord
